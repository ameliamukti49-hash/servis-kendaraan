from django import forms
from .models import Mekanik, WorkOrder


class MekanikForm(forms.ModelForm):
    class Meta:
        model = Mekanik
        fields = ['nama', 'keahlian', 'no_hp', 'alamat', 'status']

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = [
            'booking',
            'mekanik',
            'diagnosa',
            'tindakan',
            'status',
            'tanggal_selesai'
        ]

class DetailServisForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = [
            'diagnosa',
            'tindakan',
            'status',
            'tanggal_selesai',
        ]