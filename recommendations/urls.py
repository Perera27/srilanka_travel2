from django.urls import path
from . import views

app_name = 'recommendations'

urlpatterns = [
    path('', views.get_recommendations, name='get_recommendations'),
    path('popular/', views.popular_destinations, name='popular'),
]
