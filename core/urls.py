from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('safety/', views.safety_tips, name='safety'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
]