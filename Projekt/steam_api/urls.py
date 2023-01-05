from django.urls import path
from . import views

app_name = "steam_api"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('user/', views.UserViewList.as_view(), name='user_list'),
    path('user/<pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('changeUID/<pk>', views.Add_Uid.as_view(), name='changeUID'),
]
