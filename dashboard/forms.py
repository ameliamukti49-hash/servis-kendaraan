# dashboard/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserMasterForm(forms.ModelForm):
    """ Form Utama untuk Create & Update User bawaan Django """
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control-modern'}), required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control-modern', 'placeholder': 'Username unik'}),
            'email': forms.EmailInput(attrs={'class': 'form-control-modern', 'placeholder': 'email@bengkelku.com'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control-modern', 'placeholder': 'Nama Depan'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control-modern', 'placeholder': 'Nama Belakang'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input ms-2', 'role': 'switch'}),
        }

class UserProfileForm(forms.ModelForm):
    """ Form Ekstensi untuk Role dan Foto Profil """
    class Meta:
        model = UserProfile
        fields = ['role', 'no_telepon', 'foto']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select form-control-modern'}),
            'no_telepon': forms.TextInput(attrs={'class': 'form-control-modern', 'placeholder': '08123456789'}),
            'foto': forms.FileInput(attrs={'class': 'form-control form-control-modern'}),
        }