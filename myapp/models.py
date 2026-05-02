from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.conf import settings

class customer_model(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    mobileno = models.CharField(max_length=15)
    address = models.TextField() 
    photo = models.ImageField(upload_to='customer_photos/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.photo and self.id:
            # Delete old photo if exists
            try:
                old_instance = customer_model.objects.get(id=self.id)
                if old_instance.photo and old_instance.photo != self.photo:
                    if os.path.isfile(old_instance.photo.path):
                        os.remove(old_instance.photo.path)
            except customer_model.DoesNotExist:
                pass
            
            # Rename photo file
            ext = self.photo.name.split('.')[-1]
            filename = f"{self.id}_{self.username}.{ext}"
            self.photo.name = f"customer_photos/{filename}"
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete photo file when customer is deleted
        if self.photo:
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)
        super().delete(*args, **kwargs)

class per_km_price_model(models.Model):
    km = models.IntegerField()
    classs = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.km}km - {self.classs} - ₹{self.price}"

class city_model(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class starting_ending_km_model(models.Model):
    starting = models.ForeignKey(city_model, on_delete=models.CASCADE, related_name='starting_city')
    ending = models.ForeignKey(city_model, on_delete=models.CASCADE, related_name='ending_city')
    km = models.IntegerField()

    def __str__(self):
        return f"{self.starting} to {self.ending} - {self.km}km" 

class booking_details_model(models.Model):
    customer = models.ForeignKey(customer_model, on_delete=models.CASCADE)
    date = models.DateField()
    starting = models.ForeignKey(city_model, on_delete=models.CASCADE, related_name='booking_start')
    ending = models.ForeignKey(city_model, on_delete=models.CASCADE, related_name='booking_end')
    classs = models.CharField(max_length=50)
    per_tik_cost = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_tickets = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer.username} - {self.starting} to {self.ending}"

class cancel_booking_model(models.Model):
    customer = models.ForeignKey(customer_model, on_delete=models.CASCADE)
    date = models.DateField()
    starting = models.ForeignKey(city_model, on_delete=models.CASCADE, related_name='cancel_start')
    ending = models.ForeignKey(city_model, on_delete=models.CASCADE, related_name='cancel_end')
    classs = models.CharField(max_length=50)
    per_tik_cost = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_tickets = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cancel_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cancelled - {self.customer.username}"