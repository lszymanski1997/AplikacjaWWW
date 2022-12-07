from django.urls import path, include

from . import views

urlpatterns = [
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path("osoby/update/<int:pk>", views.osoba_update_delete),
    path("osoby/delete/<int:pk>", views.osoba_update_delete),
]