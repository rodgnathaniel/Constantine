from django.urls import path

from . import views

app_name = 'boat'

urlpatterns = [
    path('', views.boat_view, name='home'),
    path('save_game/', views.save_game, name='save_game'),
    path('scores/', views.scores_view, name='scores'),
    path('instructions/', views.instructions_view, name='instructions')
]
