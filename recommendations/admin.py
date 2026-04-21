from django.contrib import admin
from .models import TravelHistory

@admin.register(TravelHistory)
class TravelHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'destination', 'visited', 'viewed_at']
