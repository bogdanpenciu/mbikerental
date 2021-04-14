from django.shortcuts import render
from django.views.generic import ListView
# from Garage.models import Motorcycles
from django.http import HttpResponse


# class homepage(ListView):
#     model = Motorcycles
#     template_name = 'HOME.html'
#     context_object_name = 'motorcycles'
#
#     def get_queryset(self):
#         return Motorcycles.objects.all()



def homepage(request):

    return render(request, 'HOME.html')


