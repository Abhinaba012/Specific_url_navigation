from django.urls import path
from manutd.views import *

app_name = 'Manutd'

urlpatterns = [
    path('manutd/', manutd, name='manutd'),
]