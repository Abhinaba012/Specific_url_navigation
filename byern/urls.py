from django.urls import path
from byern.views import *

app_name = 'Byern'

urlpatterns = [
    path('byern/', byern, name='byern'),
]