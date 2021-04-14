from django.contrib import admin
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.urls import path


from accounts.views import LoginViewCustom, SignUp, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginViewCustom.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile')

]