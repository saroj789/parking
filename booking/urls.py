
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.booking,name='booking'),
    path("confirm_booking",views.confirm_booking,name='confirm_booking'),

]