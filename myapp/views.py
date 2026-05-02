from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count
from .models import *
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'index.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        mobileno = request.POST['mobileno']
        address = request.POST['address']
        photo = request.FILES.get('photo')

        if customer_model.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('user_signup')

        user = customer_model.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            gender=gender,
            mobileno=mobileno,
            address=address
        )
        
        if photo:
            user.photo = photo
            user.save()

        messages.success(request, 'Successfully new user created')
        return redirect('user_login')
    
    return render(request, 'user_signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username and password')
    
    return render(request, 'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def password_change(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        
        user = request.user
        
        if user.check_password(old_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully')
                return redirect('index')
            else:
                messages.error(request, 'New passwords do not match')
        else:
            messages.error(request, 'Old password is incorrect')
    
    return render(request, 'password_change.html')

@login_required(login_url='/login')
def customer_profile_update(request):
    user = request.user
    
    if request.method == 'POST':
        user.dob = request.POST.get('dob')
        user.mobileno = request.POST.get('mobileno')
        user.address = request.POST.get('address')
        
        if 'photo' in request.FILES:
            user.photo = request.FILES.get('photo')
        
        user.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('dashboard')
    
    return render(request, 'user_profile_update.html', {'user': user})

@login_required(login_url='/login')
def dashboard(request):
    user = request.user
    bookings = booking_details_model.objects.filter(customer=user).order_by('-date')
    total_bookings = bookings.count()
    total_amount = bookings.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    
    context = {
        'bookings': bookings,
        'total_bookings': total_bookings, 
        'total_amount': total_amount
    }
    return render(request, 'dashboard.html', context)

@login_required
def booking_details(request):
    if request.method == 'POST':
        date = request.POST['date']
        starting_id = request.POST['starting']
        ending_id = request.POST['ending']
        classs = request.POST['classs']
        no_of_tickets = int(request.POST['no_of_tickets'])
        
        starting_city = city_model.objects.get(id=starting_id)
        ending_city = city_model.objects.get(id=ending_id)
        
        # Calculate distance and price
        try:
            distance_obj = starting_ending_km_model.objects.get(starting=starting_city, ending=ending_city)
            km = distance_obj.km
        except starting_ending_km_model.DoesNotExist:
            messages.error(request, 'Route not available')
            return redirect('booking_details')
        
        try:
            price_obj = per_km_price_model.objects.get(km=km, classs=classs)
            per_tik_cost = price_obj.price
        except per_km_price_model.DoesNotExist: 
            messages.error(request, 'Price not available for this route and class')
            return redirect('booking_details')
        
        total_amount = per_tik_cost * no_of_tickets
        
        booking = booking_details_model.objects.create(
            customer=request.user,
            date=date,
            starting=starting_city,
            ending=ending_city,
            classs=classs,
            per_tik_cost=per_tik_cost,
            no_of_tickets=no_of_tickets,
            total_amount=total_amount
        )
        
        messages.success(request, 'Booking confirmed successfully')
        return redirect('dashboard')
    
    cities = city_model.objects.all()
    classes = per_km_price_model.objects.values_list('classs', flat=True).distinct()
    
    return render(request, 'booking_details.html', {
        'cities': cities,
        'classes': classes
    })

@login_required
def cancel_ticket(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(booking_details_model, id=booking_id, customer=request.user)
        
        # Create cancel booking record
        cancel_booking_model.objects.create(
            customer=request.user,
            date=booking.date,
            starting=booking.starting,
            ending=booking.ending,
            classs=booking.classs,
            per_tik_cost=booking.per_tik_cost,
            no_of_tickets=booking.no_of_tickets,
            total_amount=booking.total_amount
        )
        
        # Delete the booking
        booking.delete()
        
        messages.success(request, 'Successfully cancel your booking')
    
    return redirect('dashboard')

def get_price(request):
    if request.method == 'GET':
        starting_id = request.GET.get('starting')
        ending_id = request.GET.get('ending')
        classs = request.GET.get('classs')
        
        try:
            starting_city = city_model.objects.get(id=starting_id)
            ending_city = city_model.objects.get(id=ending_id)
            
            distance_obj = starting_ending_km_model.objects.get(starting=starting_city, ending=ending_city)
            km = distance_obj.km
            
            price_obj = per_km_price_model.objects.get(km=km, classs=classs)
            
            return JsonResponse({
                'price_per_ticket': float(price_obj.price),
                'distance': km
            })
        except Exception as e:
            return JsonResponse({'error': 'Price not available'}, status=400)