
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.slots),
    path("slots/",views.slots, name='slots'),
]