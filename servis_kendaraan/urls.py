from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts
    path('', include('accounts.urls')),

    # Dashboard
    path('dashboard/', include('dashboard.urls')),

    # Booking & Kendaraan
    path('', include('booking.urls')),

    # Mekanik
    path('mekanik/', include('mekanik.urls')),

    # Pembayaran
    path('pembayaran/', include('pembayaran.urls')),
]