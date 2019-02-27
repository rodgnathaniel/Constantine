from django.urls import path

from . import views

app_name = 'boat'

urlpatterns = [
    path('', views.boat_view, name='home'),
    path('level_2/', views.level_2_view, name='level_2'),
    path('level_3/', views.level_3_view, name='level_3'),
    path('save_game/', views.save_game, name='save_game'),
    path('scores/', views.scores_view, name='scores'),
    path('instructions/', views.instructions_view, name='instructions')
]
