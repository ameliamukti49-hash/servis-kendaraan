from django.conf import settings
from django.db import models
from django.apps import apps

# =====================================================================
# 1. MODEL UTAMA INTERNAL (Khusus Tugas Anggota 5)
# =====================================================================

class LogAktivitasAdmin(models.Model):
    # Menggunakan settings.AUTH_USER_MODEL agar dukung Custom User buatan Anggota 1
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='logs_admin')
    aktivitas = models.CharField(max_length=255)
    keterangan = models.TextField(blank=True, null=True)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Log Aktivitas Admin"

    def __str__(self):
        return f"{self.admin} - {self.aktivitas}"


# =====================================================================
# 2. MODEL CADANGAN ANTI-CRASH (Milik Anggota 2, 3, & 4)
# =====================================================================
# Logika di bawah ini memeriksa apakah app milik anggota lain sudah ada di proyek.
# Jika BELUM ADA, Django akan membuatkan tabel bayangan agar proyek bisa di-run.

if not apps.is_installed('booking'):
    class Kendaraan(models.Model):
        # Diperbaiki: Menggunakan settings.AUTH_USER_MODEL
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        merk = models.CharField(max_length=50)
        tipe = models.CharField(max_length=50)
        plat_nomor = models.CharField(max_length=15)
        
        class Meta:
            managed = True

    class BookingServis(models.Model):
        STATUS_CHOICES = [
            ('Menunggu', 'Menunggu'),
            ('Proses', 'Proses'),
            ('Selesai', 'Selesai'),
        ]
        # Diperbaiki: Menggunakan settings.AUTH_USER_MODEL
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        kendaraan = models.ForeignKey(Kendaraan, on_delete=models.CASCADE)
        mekanik = models.ForeignKey('Mekanik', on_delete=models.SET_NULL, null=True)
        tanggal = models.DateField()
        jam = models.TimeField()
        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Menunggu')
        
        class Meta:
            managed = True

if not apps.is_installed('mekanik'):
    class Mekanik(models.Model):
        nama = models.CharField(max_length=100)
        keahlian = models.CharField(max_length=100)
        status_aktif = models.BooleanField(default=True)
        
        class Meta:
            managed = True

    class WorkOrder(models.Model):
        STATUS_WO = [
            ('Antrean', 'Antrean'),
            ('Dikerjakan', 'Dikerjakan'),
            ('Selesai', 'Selesai'),
        ]
        booking = models.ForeignKey('BookingServis' if not apps.is_installed('booking') else 'booking.BookingServis', on_delete=models.CASCADE)
        mekanik = models.ForeignKey(Mekanik, on_delete=models.CASCADE)
        diagnosa = models.TextField(blank=True, null=True)
        tindakan = models.TextField(blank=True, null=True)
        status = models.CharField(max_length=20, choices=STATUS_WO, default='Antrean')
        tanggal_update = models.DateTimeField(auto_now=True)
        
        class Meta:
            managed = True

if not apps.is_installed('pembayaran'):
    class Pembayaran(models.Model):
        STATUS_BAYAR = [
            ('Belum Lunas', 'Belum Lunas'),
            ('Lunas', 'Lunas'),
        ]
        booking = models.ForeignKey('BookingServis' if not apps.is_installed('booking') else 'booking.BookingServis', on_delete=models.CASCADE)
        metode = models.CharField(max_length=50, default='Tunai')
        total_biaya = models.IntegerField(default=0)
        status = models.CharField(max_length=20, choices=STATUS_BAYAR, default='Belum Lunas')
        tanggal_bayar = models.DateField(auto_now_add=True)
        
        class Meta:
            managed = True