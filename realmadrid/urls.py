from django.urls import path
from realmadrid.views import *

app_name = 'Real'

urlpatterns = [
    path('real/', real, name='real'),
]