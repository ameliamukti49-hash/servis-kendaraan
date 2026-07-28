from django.db import models
from django.conf import settings


class UserProfile(models.Model):

    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('service_advisor', 'Service Advisor'),
        ('mekanik', 'Mekanik'),
        ('kasir', 'Kasir'),
        ('pelanggan', 'Pelanggan'),
    )


    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )


    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default='pelanggan'
    )


    foto = models.ImageField(
        upload_to='profile_pics/',
        default='avatar.png',
        null=True,
        blank=True
    )


    no_telepon = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )


    def __str__(self):
        return f"{self.user.username} - {self.role}"