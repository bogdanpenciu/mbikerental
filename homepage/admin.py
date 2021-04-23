from django.contrib import admin

from .models import Moto, Reservation, PriceIncrease, MotoReview

admin.site.register(Moto)
admin.site.register(Reservation)
admin.site.register(PriceIncrease)
admin.site.register(MotoReview)
