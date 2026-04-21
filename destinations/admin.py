from django.contrib import admin
from .models import Destination, Category, Province, DestinationImage, FavouriteDestination


class DestinationImageInline(admin.TabularInline):
    model = DestinationImage
    extra = 3


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'province', 'budget_level', 'is_hidden_gem', 'is_featured', 'is_active', 'view_count']
    list_filter = ['category', 'province', 'budget_level', 'difficulty', 'is_hidden_gem', 'is_featured', 'is_active']
    search_fields = ['name', 'description', 'city', 'tags']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_featured', 'is_active', 'is_hidden_gem']
    inlines = [DestinationImageInline]
    fieldsets = (
        ('Basic Info', {'fields': ('name', 'slug', 'category', 'province', 'short_description', 'description')}),
        ('Location', {'fields': ('address', 'city', 'latitude', 'longitude')}),
        ('Media', {'fields': ('featured_image',)}),
        ('Details', {'fields': ('budget_level', 'difficulty', 'best_time_to_visit', 'opening_hours', 'entry_fee', 'tags')}),
        ('Dress Code', {'fields': ('requires_dress_code', 'dress_code_description'), 'classes': ('collapse',)}),
        ('Safety', {'fields': ('safety_notes',), 'classes': ('collapse',)}),
        ('Flags', {'fields': ('is_hidden_gem', 'is_featured', 'is_active')}),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'icon']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(DestinationImage)
class DestinationImageAdmin(admin.ModelAdmin):
    list_display = ['destination', 'caption']
    list_filter = ['destination']
    search_fields = ['destination__name', 'caption']


@admin.register(FavouriteDestination)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'destination', 'added_at']
    list_filter = ['destination__category']