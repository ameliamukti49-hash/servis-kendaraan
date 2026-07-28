from django.db import models
from mekanik.models import WorkOrder

class Sparepart(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nama


class JasaServis(models.Model):
    nama = models.CharField(max_length=100)
    biaya = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama

class DetailSparepart(models.Model):
    workorder = models.ForeignKey(
        WorkOrder,
        on_delete=models.CASCADE,
        related_name='detail_sparepart'
    )

    sparepart = models.ForeignKey(
        Sparepart,
        on_delete=models.CASCADE
    )

    jumlah = models.PositiveIntegerField(default=1)

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.workorder} - {self.sparepart}"

class DetailJasa(models.Model):
    workorder = models.ForeignKey(
        WorkOrder,
        on_delete=models.CASCADE,
        related_name='detail_jasa'
    )

    jasa = models.ForeignKey(
        JasaServis,
        on_delete=models.CASCADE
    )

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.workorder} - {self.jasa}"

class Pembayaran(models.Model):

    METODE = (
        ('Cash', 'Cash'),
        ('Transfer', 'Transfer'),
        ('QRIS', 'QRIS'),
    )

    workorder = models.OneToOneField(
        WorkOrder,
        on_delete=models.CASCADE,
        related_name='pembayaran'
    )

    total_sparepart = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total_jasa = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total_bayar = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    metode = models.CharField(
        max_length=20,
        choices=METODE
    )

    tanggal_bayar = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        default='Lunas'
    )

    def __str__(self):
        return f"Pembayaran {self.workorder}"