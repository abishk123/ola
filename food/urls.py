from food.views import *
from django.urls import path

app_name='anything'

urlpatterns=[
    path('nonVeg/',nonVeg,name='nonVeg'),
    path('veg/',veg,name='veg'),
]