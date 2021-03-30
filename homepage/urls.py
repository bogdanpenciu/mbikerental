from django.urls import path, include

from homepage.views import home_page

app_name = "accounts"

urlpatterns = [
    path('', home_page, name="shop"),
]