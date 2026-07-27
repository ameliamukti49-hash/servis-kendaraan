from django import forms
from .models import Kendaraan, BookingServis


class KendaraanForm(forms.ModelForm):

    class Meta:
        model = Kendaraan
        fields = [
            'jenis',
            'merk',
            'tipe',
            'tahun',
            'nomor_polisi',
            'warna',
            'nomor_rangka',
            'nomor_mesin',
        ]

        widgets = {

            'jenis': forms.Select(attrs={
                'class': 'form-select'
            }),

            'merk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contoh: Honda'
            }),

            'tipe': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contoh: Beat Deluxe'
            }),

            'tahun': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '2024'
            }),

            'nomor_polisi': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'N 1234 AB'
            }),

            'warna': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Hitam'
            }),

            'nomor_rangka': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'nomor_mesin': forms.TextInput(attrs={
                'class': 'form-control'
            }),

        }


class BookingServisForm(forms.ModelForm):

    class Meta:
        model = BookingServis
        fields = [
            'kendaraan',
            'tanggal_booking',
            'jam_booking',
            'keluhan'
        ]

        widgets = {

            'kendaraan': forms.Select(attrs={
                'class': 'form-select'
            }),

            'tanggal_booking': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'jam_booking': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),

            'keluhan': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tuliskan keluhan kendaraan...'
            }),

        }

    def clean(self):
        cleaned_data = super().clean()

        tanggal = cleaned_data.get('tanggal_booking')
        jam = cleaned_data.get('jam_booking')

        if tanggal and jam:

            booking = BookingServis.objects.filter(
                tanggal_booking=tanggal,
                jam_booking=jam
            )

            if self.instance.pk:
                booking = booking.exclude(pk=self.instance.pk)

            if booking.exists():
                raise forms.ValidationError(
                    "Jadwal pada tanggal dan jam tersebut sudah dibooking."
                )

        return cleaned_data