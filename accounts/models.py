from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('service_advisor', 'Service Advisor'),
    ('pelanggan', 'Pelanggan'),
    ('mekanik', 'Mekanik'),
    ('kasir', 'Kasir'),
)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='pelanggan'
    )

    def __str__(self):
        return self.username