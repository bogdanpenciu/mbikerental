from datetime import datetime, date

from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from .forms import ReservationForm
from .models import Moto, Reservation, PriceIncrease
from django.template import loader
from django.contrib.auth.mixins import PermissionRequiredMixin



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

    def form_valid(self, form):
        reservation= form.save(commit=False)
        reservation.customer=self.request.user
        reservation.save()
        return HttpResponseRedirect(self.success_url)


class ReservationCompView(TemplateView):
 template_name = "homepage/reservation_complete.html"


class ReservationView(PermissionRequiredMixin, ListView):
    template_name = 'homepage/reservationlist.html'
    model = Reservation
    context_object_name = 'reservation_list'
    permission_required = 'homepage:reslist'

    def get_queryset(self):
        return Reservation.objects.all()

class AddMoto(PermissionRequiredMixin, CreateView):
    model = Moto
    template_name = 'homepage/add_new_moto.html'
    success_url = reverse_lazy('homepage:home')
    fields = '__all__'
    permission_required = 'homepage:addnewmoto'

class EditMoto(PermissionRequiredMixin, UpdateView):
    model = Moto
    template_name = 'homepage/update_moto.html'
    success_url = reverse_lazy('homepage:home')
    fields = '__all__'
    permission_required = 'homepage:editmoto'

class PriceList(ListView):
    template_name = 'homepage/pricelist.html'
    model = PriceIncrease
    context_object_name = 'price_list'

    def get_queryset(self):
        return PriceIncrease.objects.all()

class AddNewPrice(PermissionRequiredMixin, CreateView):
    model = PriceIncrease
    template_name = 'homepage/add_new_price.html'
    success_url = reverse_lazy('homepage:pricelist')
    fields = '__all__'
    permission_required = 'homepage:addnewprice'

class EditPrice(PermissionRequiredMixin, UpdateView):
    model = PriceIncrease
    template_name = 'homepage/update_price.html'
    success_url = reverse_lazy('homepage:pricelist')
    fields = '__all__'
    permission_required = 'homepage:editprice'

class DeletePrice(PermissionRequiredMixin, DeleteView):
    model = PriceIncrease
    template_name = 'homepage/delete_price.html'
    success_url = reverse_lazy('homepage:pricelist')
    context_object_name = 'price'
    permission_required = 'homepage:editdelete'

