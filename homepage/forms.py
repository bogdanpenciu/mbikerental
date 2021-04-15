from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from homepage.models import Reservation


class ReservationForm(forms.ModelForm):


    class Meta:
        model = Reservation
        fields = ('moto', 'date_start', 'date_return')
        widgets = {'moto': forms.Select(attrs={'class': 'form-control'}),
                   'date_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date','required':'required'}),
                   'date_return': forms.DateInput(attrs={'class': 'form-control', 'type': 'date','required':'required'}),
                   }