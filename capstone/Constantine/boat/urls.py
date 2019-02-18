from django.urls import path

from . import views

app_name = 'boat'

urlpatterns = [
    path('', views.boat_view, name='home'),
]
