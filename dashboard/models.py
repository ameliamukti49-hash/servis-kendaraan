from django.conf import settings
from django.db import models

# =====================================================================
# 1. MODEL UTAMA INTERNAL (Khusus Tugas Anggota 5)
# =====================================================================

class LogAktivitasAdmin(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='logs_admin')
    aktivitas = models.CharField(max_length=255)
    keterangan = models.TextField(blank=True, null=True)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Log Aktivitas Admin"

    def __str__(self):
        return f"{self.admin} - {self.aktivitas}"


# =====================================================================
# 2. MODEL CADANGAN MANDIRI (Sudah Dilengkapi Paspor Unik 'related_name')
# =====================================================================

class Kendaraan(models.Model):
    # Ditambahkan related_name agar tidak tabrakan dengan app booking
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fallback_kendaraan')
    merk = models.CharField(max_length=50)
    tipe = models.CharField(max_length=50)
    plat_nomor = models.CharField(max_length=15)

class Mekanik(models.Model):
    nama = models.CharField(max_length=100)
    keahlian = models.CharField(max_length=100)
    status_aktif = models.BooleanField(default=True)

class BookingServis(models.Model):
    STATUS_CHOICES = [
        ('Menunggu', 'Menunggu'),
        ('Proses', 'Proses'),
        ('Selesai', 'Selesai'),
    ]
    # Ditambahkan related_name unik
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fallback_booking')
    kendaraan = models.ForeignKey(Kendaraan, on_delete=models.CASCADE, related_name='fallback_booking_kendaraan')
    mekanik = models.ForeignKey(Mekanik, on_delete=models.SET_NULL, null=True, blank=True, related_name='fallback_booking_mekanik')
    tanggal = models.DateField()
    jam = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Menunggu')

class WorkOrder(models.Model):
    STATUS_WO = [
        ('Antrean', 'Antrean'),
        ('Dikerjakan', 'Dikerjakan'),
        ('Selesai', 'Selesai'),
    ]
    booking = models.ForeignKey(BookingServis, on_delete=models.CASCADE, related_name='fallback_wo_booking')
    mekanik = models.ForeignKey(Mekanik, on_delete=models.CASCADE, related_name='fallback_wo_mekanik')
    diagnosa = models.TextField(blank=True, null=True)
    tindakan = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_WO, default='Antrean')
    tanggal_update = models.DateTimeField(auto_now=True)

class Pembayaran(models.Model):
    STATUS_BAYAR = [
        ('Belum Lunas', 'Belum Lunas'),
        ('Lunas', 'Lunas'),
    ]
    booking = models.ForeignKey(BookingServis, on_delete=models.CASCADE, related_name='fallback_pembayaran_booking')
    metode = models.CharField(max_length=50, default='Tunai')
    total_biaya = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_BAYAR, default='Belum Lunas')
    tanggal_bayar = models.DateField(auto_now_add=True)