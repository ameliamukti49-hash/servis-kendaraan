from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts
    path('', include('accounts.urls')),

    # Dashboard
    path('', include('dashboard.urls')),
<<<<<<< HEAD

    # Booking & Kendaraan
    path('', include('booking.urls')),
=======
    path('mekanik/', include('mekanik.urls')),
>>>>>>> 44a3a63d019cc1095a688f29fd6a3e962293bd7b
]