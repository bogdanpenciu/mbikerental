from datetime import datetime, date

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from .forms import ReservationForm, MotoReviewForm
from .models import Moto, Reservation, PriceIncrease, MotoReview
from django.template import loader
from django.contrib.auth.mixins import PermissionRequiredMixin



class Home(ListView):
    template_name = 'homepage/home.html'
    model = Moto
    context_object_name = 'moto_list'

    def get_queryset(self):
        return Moto.objects.all()

# def detail(request,  moto_id):
#     moto = get_object_or_404(Moto,  id=moto_id)
#     context = {'moto': moto}
#     return render(request, 'homepage/details.html', context)


class Detail(DetailView):
    template_name = 'homepage/details.html'
    model = Moto
    context_object_name = 'moto'

class AddReview(CreateView):
    template_name = 'homepage/add_review.html'
    form_class = MotoReviewForm
    model = MotoReview


    def form_valid(self, form):
        form.instance.moto_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('homepage:detail', kwargs={'pk': self.kwargs['pk']})




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

