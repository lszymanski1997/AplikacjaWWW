from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "steam_api"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('refresh/', views.refresh_game_list, name='refresh'),
    path('add_review/', views.add_review, name="add_review"),
    path('review/', views.review_list),
    path('game/', views.game_list),
    path('game/<int:pk>', views.game_detail),
    path('review/<int:pk>', views.review_detail),

]
