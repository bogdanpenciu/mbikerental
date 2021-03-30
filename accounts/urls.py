from django.contrib import admin
from django.urls import path, include

from accounts.views import LoginViewCustom

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginViewCustom.as_view(), name="login"),

]