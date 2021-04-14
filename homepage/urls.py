from django.urls import path

from homepage.views import Home, Detail, CreateReservation, ReservationCompView, EditMoto, AddMoto, PriceList, AddNewPrice, EditPrice, \
    ReservationView, DeletePrice

app_name='homepage'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('<int:pk>', Detail.as_view(), name='detail'),
    path('rezervation/', CreateReservation.as_view(), name='reservation'),
    path('rezcomp/', ReservationCompView.as_view(), name='rezcomp'),
    path('reslist/', ReservationView.as_view(), name='reslist'),
    path('addnewmoto/',AddMoto.as_view(), name='addnewmoto'),
    path('editmoto/<int:pk>',EditMoto.as_view(), name='editmoto'),
    path('pricelist/', PriceList.as_view(), name="pricelist"),
    path('addnewprice/',AddNewPrice.as_view(), name='addnewprice'),
    path('editprice/<int:pk>',EditPrice.as_view(), name='editprice'),
    path('deleteprice/<int:pk>',DeletePrice.as_view(), name='deleteprice'),

]
    