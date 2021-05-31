from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from homepage.models import Reservation, MotoReview, Contact


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('moto', 'date_start', 'date_return')
        widgets = {'moto': forms.Select(attrs={'class': 'form-control'}),
                   'date_start': forms.DateInput(
                       attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
                   'date_return': forms.DateInput(
                       attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}), }
        labels = {'moto': 'Select a bike from list:',}


class MotoReviewForm(ModelForm):
    class Meta:
        model = MotoReview
        fields = ('content', 'stars',)

class MsgForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'phone','e_mail', 'message',)