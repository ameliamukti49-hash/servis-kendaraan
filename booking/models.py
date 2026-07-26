from django.db import models
from django.conf import settings


class Kendaraan(models.Model):

    JENIS_KENDARAAN = (
        ('Motor', 'Motor'),
        ('Mobil', 'Mobil'),
    )

    pemilik = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='kendaraan'
    )

    jenis = models.CharField(
        max_length=20,
        choices=JENIS_KENDARAAN
    )

    merk = models.CharField(
        max_length=100
    )

    tipe = models.CharField(
        max_length=100
    )

    tahun = models.PositiveIntegerField()

    nomor_polisi = models.CharField(
        max_length=20,
        unique=True
    )

    warna = models.CharField(
        max_length=50
    )

    nomor_rangka = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    nomor_mesin = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ['-created_at']

        verbose_name = 'Kendaraan'

        verbose_name_plural = 'Data Kendaraan'

    def __str__(self):

        return f"{self.nomor_polisi} - {self.merk} {self.tipe}"


class BookingServis(models.Model):

    STATUS = (

        ('menunggu', 'Menunggu'),

        ('diproses', 'Diproses'),

        ('dikerjakan', 'Dikerjakan'),

        ('selesai', 'Selesai'),

        ('dibatalkan', 'Dibatalkan'),

    )

    kendaraan = models.ForeignKey(
        Kendaraan,
        on_delete=models.CASCADE,
        related_name='booking'
    )

    tanggal_booking = models.DateField()

    jam_booking = models.TimeField()

    keluhan = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='menunggu'
    )

    estimasi_selesai = models.DateField(
        blank=True,
        null=True
    )

    catatan_admin = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ['-tanggal_booking', '-jam_booking']

        verbose_name = 'Booking Servis'

        verbose_name_plural = 'Booking Servis'

    def __str__(self):

        return f"{self.kendaraan.nomor_polisi} - {self.tanggal_booking} ({self.status})"
    