from django import forms
from .models import Sparepart, JasaServis, Pembayaran
from .models import Pembayaran

class SparepartForm(forms.ModelForm):

    class Meta:
        model = Sparepart
        fields = [
            'nama',
            'harga',
            'stok'
        ]

        widgets = {
            'nama': forms.TextInput(attrs={
                'class':'form-control'
            }),

            'harga': forms.NumberInput(attrs={
                'class':'form-control'
            }),

            'stok': forms.NumberInput(attrs={
                'class':'form-control'
            }),
        }



class JasaServisForm(forms.ModelForm):

    class Meta:
        model = JasaServis

        fields = [
            'nama',
            'biaya'
        ]

        widgets = {

            'nama': forms.TextInput(attrs={
                'class':'form-control'
            }),

            'biaya': forms.NumberInput(attrs={
                'class':'form-control'
            }),

        }



class PembayaranForm(forms.ModelForm):

    class Meta:

        model = Pembayaran

        fields = [
            'workorder',
            'total_sparepart',
            'total_jasa',
            'metode',
        ]


        widgets = {

            'workorder': forms.Select(attrs={
                'class':'form-select'
            }),

            'total_sparepart': forms.NumberInput(attrs={
                'class':'form-control'
            }),

            'total_jasa': forms.NumberInput(attrs={
                'class':'form-control'
            }),

            'metode': forms.Select(attrs={
                'class':'form-select'
            }),

        }

class PembayaranForm(forms.ModelForm):

    class Meta:
        model = Pembayaran

        fields = [
            'workorder',
            'total_sparepart',
            'total_jasa',
            'metode',
        ]

        widgets = {

            'workorder': forms.Select(attrs={
                'class':'form-select'
            }),

            'total_sparepart': forms.NumberInput(attrs={
                'class':'form-control'
            }),

            'total_jasa': forms.NumberInput(attrs={
                'class':'form-control'
            }),

            'metode': forms.Select(attrs={
                'class':'form-select'
            }),
        }