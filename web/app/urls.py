from django.urls import path
from .views import home

urlpatterns = [
    path('home/', view = home, name = 'home')
]