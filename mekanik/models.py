from django.db import models
from booking.models import BookingServis


class Mekanik(models.Model):
    STATUS_CHOICES = [
        ('Aktif', 'Aktif'),
        ('Tidak Aktif', 'Tidak Aktif'),
    ]

    nama = models.CharField(max_length=100)
    keahlian = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=15)
    alamat = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Aktif'
    )

    def __str__(self):
        return self.nama

class WorkOrder(models.Model):

    STATUS = (
        ('diproses', 'Diproses'),
        ('dikerjakan', 'Dikerjakan'),
        ('selesai', 'Selesai'),
    )

    booking = models.OneToOneField(
        BookingServis,
        on_delete=models.CASCADE,
        related_name='workorder'
    )

    mekanik = models.ForeignKey(
        Mekanik,
        on_delete=models.CASCADE,
        related_name='workorder'
    )

    diagnosa = models.TextField()

    tindakan = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='diproses'
    )

    tanggal_mulai = models.DateField(auto_now_add=True)

    tanggal_selesai = models.DateField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"WO - {self.booking.kendaraan.nomor_polisi}"