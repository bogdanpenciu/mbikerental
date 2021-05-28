from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['email', 'first_name', 'last_name', 'username', ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birthday', 'licence_valid_date', 'licence_cat', 'picture')
        widgets = {
                   'birthday': forms.DateInput(
                       attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
                   'licence_valid_date': forms.DateInput(
                       attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
                    'picture': forms.FileInput(
                        attrs={'class': 'form-control', 'id' : 'input-file' })
        }

