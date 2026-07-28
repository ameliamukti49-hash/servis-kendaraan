from django import forms
from .models import Sparepart, JasaServis


class SparepartForm(forms.ModelForm):
    class Meta:
        model = Sparepart
        fields = ['nama', 'harga', 'stok']


class JasaServisForm(forms.ModelForm):
    class Meta:
        model = JasaServis
        fields = ['nama', 'biaya']