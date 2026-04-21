from django.urls import path
from . import views

app_name = 'destinations'

urlpatterns = [
    path('', views.destination_list, name='list'),
    path('hidden-gems/', views.hidden_gems, name='hidden_gems'),
    path('favourites/', views.my_favourites, name='favourites'),
    path('<slug:slug>/', views.destination_detail, name='detail'),
    path('<slug:slug>/favourite/', views.toggle_favourite, name='toggle_favourite'),
]
