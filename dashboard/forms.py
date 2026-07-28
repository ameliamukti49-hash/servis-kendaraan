from django import forms
from django.contrib.auth import get_user_model

from .models import UserProfile


User = get_user_model()



class UserMasterForm(forms.ModelForm):
    """
    Form untuk membuat dan edit user utama
    """

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        ),
        required=False
    )


    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
            'is_active'
        ]


        widgets = {

            'username': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Username'
                }
            ),


            'email': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Email'
                }
            ),


            'first_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nama Depan'
                }
            ),


            'last_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nama Belakang'
                }
            ),


            'role': forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),


            'is_active': forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            )

        }



    def save(self, commit=True):

        user = super().save(commit=False)


        password = self.cleaned_data.get(
            'password'
        )


        if password:

            user.set_password(password)


        if commit:

            user.save()


        return user







class UserProfileForm(forms.ModelForm):
    """
    Form tambahan profil user
    """


    class Meta:

        model = UserProfile


        fields = [
            'no_telepon',
            'foto'
        ]


        widgets = {


            'no_telepon': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'08123456789'
                }
            ),


            'foto': forms.FileInput(
                attrs={
                    'class':'form-control'
                }
            )

        }