# i have created this file 

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('<int:id>/', views.moviePage, name="moviePage"),
]