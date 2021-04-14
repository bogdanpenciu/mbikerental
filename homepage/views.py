from datetime import datetime, date

from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from .forms import ReservationForm
from .models import Moto, Reservation, PriceIncrease
from django.template import loader



class Home(ListView):
    template_name = 'homepage/home.html'
    model = Moto
    context_object_name = 'moto_list'

    def get_queryset(self):
        return Moto.objects.all()


class Detail(DetailView):
    template_name = 'homepage/details.html'
    model = Moto
    context_object_name = 'detail'

class CreateReservation(CreateView):
    template_name = 'homepage/reservation.html'
    form_class = ReservationForm
    model = Reservation
    success_url = reverse_lazy('homepage:rezcomp')

class ReservationCompView(TemplateView):
 template_name = "homepage/reservation_complete.html"


class ReservationView(ListView):
    template_name = 'homepage/reservationlist.html'
    model = Reservation
    context_object_name = 'reservation_list'

    def get_queryset(self):
        return Reservation.objects.all()

class AddMoto(CreateView):
    model = Moto
    template_name = 'homepage/add_new_moto.html'
    success_url = reverse_lazy('homepage:home')
    fields = '__all__'

class EditMoto(UpdateView):
    model = Moto
    template_name = 'homepage/update_moto.html'
    success_url = reverse_lazy('homepage:home')
    fields = '__all__'

class PriceList(ListView):
    template_name = 'homepage/pricelist.html'
    model = PriceIncrease
    context_object_name = 'price_list'

    def get_queryset(self):
        return PriceIncrease.objects.all()

class AddNewPrice(CreateView):
    model = PriceIncrease
    template_name = 'homepage/add_new_price.html'
    success_url = reverse_lazy('homepage:pricelist')
    fields = '__all__'

class EditPrice(UpdateView):
    model = PriceIncrease
    template_name = 'homepage/update_price.html'
    success_url = reverse_lazy('homepage:pricelist')
    fields = '__all__'

class DeletePrice(DeleteView):
    model = PriceIncrease
    template_name = 'homepage/delete_price.html'
    success_url = reverse_lazy('homepage:pricelist')
    context_object_name = 'price'

