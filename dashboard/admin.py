from django.contrib import admin
from .models import LogAktivitasAdmin, Kendaraan, BookingServis, Mekanik, WorkOrder, Pembayaran

admin.site.register(LogAktivitasAdmin)
admin.site.register(Kendaraan)
admin.site.register(BookingServis)
admin.site.register(Mekanik)
admin.site.register(WorkOrder)
admin.site.register(Pembayaran)
