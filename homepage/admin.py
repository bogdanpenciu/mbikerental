from django.contrib import admin

from .models import Moto, Reservation, PriceIncrease

admin.site.register(Moto)
admin.site.register(Reservation)
admin.site.register(PriceIncrease)