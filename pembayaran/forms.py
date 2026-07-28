from django import forms
from .models import (
    Sparepart,
    JasaServis,
    Pembayaran,
    DetailSparepart,
    DetailJasa,
)


class SparepartForm(forms.ModelForm):
    class Meta:
        model = Sparepart
        fields = [
            'nama',
            'harga',
            'stok',
        ]


class JasaServisForm(forms.ModelForm):
    class Meta:
        model = JasaServis
        fields = [
            'nama',
            'biaya',
        ]


class PembayaranForm(forms.ModelForm):
    class Meta:
        model = Pembayaran
        fields = [
            'metode',
        ]


class DetailSparepartForm(forms.ModelForm):
    class Meta:
        model = DetailSparepart
        fields = [
            'sparepart',
            'jumlah',
        ]


class DetailJasaForm(forms.ModelForm):
    class Meta:
        model = DetailJasa
        fields = [
            'jasa',
        ]