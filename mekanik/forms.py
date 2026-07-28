from django import forms
from .models import Mekanik, WorkOrder



class MekanikForm(forms.ModelForm):

    class Meta:

        model = Mekanik

        fields = [
            'nama',
            'keahlian',
            'no_hp',
            'alamat',
            'status'
        ]


        widgets = {

            'nama': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nama mekanik'
                }
            ),


            'keahlian': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Keahlian mekanik'
                }
            ),


            'no_hp': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nomor HP'
                }
            ),


            'alamat': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':3,
                    'placeholder':'Alamat mekanik'
                }
            ),


            'status': forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),

        }





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


        widgets = {


            'booking': forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),



            'mekanik': forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),



            'diagnosa': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':4,
                    'placeholder':'Masukkan diagnosa kendaraan'
                }
            ),



            'tindakan': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':4,
                    'placeholder':'Masukkan tindakan servis'
                }
            ),



            'status': forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),



            'tanggal_selesai': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date'
                }
            ),

        }





class DetailServisForm(forms.ModelForm):

    class Meta:

        model = WorkOrder


        fields = [
            'diagnosa',
            'tindakan',
            'status',
            'tanggal_selesai',
        ]


        widgets = {


            'diagnosa': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':4
                }
            ),


            'tindakan': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':4
                }
            ),


            'status': forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),


            'tanggal_selesai': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date'
                }
            ),

        }