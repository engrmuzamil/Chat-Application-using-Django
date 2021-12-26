from django.urls import path
from . views import *
urlpatterns = [
    path('', messages_page),
    path('search/', search, name='search'),
]
