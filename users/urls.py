from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
    path('', views.index), #https://api-servis-mobil.vercel.app
    path('add/', views.Add, name='add'),
    path('list/',views.List, name='list'),
]