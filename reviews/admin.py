from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'destination', 'rating', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_approved']
    list_editable = ['is_approved']
    search_fields = ['user__username', 'destination__name', 'title']
