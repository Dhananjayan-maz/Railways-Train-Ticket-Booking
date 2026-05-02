from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('password_change/', views.password_change, name='password_change'),
    path('customer_profile_update/', views.customer_profile_update, name='customer_profile_update'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('booking_details/', views.booking_details, name='booking_details'),
    path('cancel_ticket/<int:booking_id>/', views.cancel_ticket, name='cancel_ticket'),
    path('get_price/', views.get_price, name='get_price'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)