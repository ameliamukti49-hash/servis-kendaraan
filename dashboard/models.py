# dashboard/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Administrator'),
        ('Service Advisor', 'Service Advisor'),
        ('Mekanik', 'Mekanik'),
        ('Kasir', 'Kasir'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Mekanik')
    foto = models.ImageField(upload_to='profile_pics/', default='avatar.png', null=True, blank=True)
    no_telepon = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"