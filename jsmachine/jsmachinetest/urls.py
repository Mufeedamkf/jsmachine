from django.urls import path
from . import views

app_name='jsmachinetest'

urlpatterns=[
    path('jsmachine',views.jsmachine,name='jsmachine'),

]