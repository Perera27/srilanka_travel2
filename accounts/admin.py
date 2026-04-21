from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'traveller_type', 'nationality', 'preferred_budget']
    list_filter = ['traveller_type']
    search_fields = ['user__username', 'user__email', 'nationality']
