from django.urls import path, include

from Garage.views import homepage

app_name='Garage'

urlpatterns = [
    path('', homepage, name="home")
    ]