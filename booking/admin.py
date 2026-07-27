from django.contrib import admin
from .models import Kendaraan, BookingServis


@admin.register(Kendaraan)
class KendaraanAdmin(admin.ModelAdmin):

    list_display = (
        'nomor_polisi',
        'pemilik',
        'jenis',
        'merk',
        'tipe',
        'tahun',
        'warna',
    )

    search_fields = (
        'nomor_polisi',
        'merk',
        'tipe',
    )

    list_filter = (
        'jenis',
        'merk',
    )


@admin.register(BookingServis)
class BookingServisAdmin(admin.ModelAdmin):

    list_display = (
        'kendaraan',
        'tanggal_booking',
        'jam_booking',
        'status',
    )

    search_fields = (
        'kendaraan__nomor_polisi',
    )

    list_filter = (
        'status',
        'tanggal_booking',
    )