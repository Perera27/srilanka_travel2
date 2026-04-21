from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    CATEGORY_CHOICES = [
        ('beach', 'Beach & Coastal'),
        ('wildlife', 'Wildlife & Nature'),
        ('cultural', 'Cultural & Heritage'),
        ('religious', 'Religious & Spiritual'),
        ('adventure', 'Adventure & Trekking'),
        ('historical', 'Historical Sites'),
        ('scenic', 'Scenic & Viewpoints'),
        ('waterfalls', 'Waterfalls'),
        ('food', 'Food & Cuisine'),
    ]
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    category_type = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='cultural')
    icon = models.CharField(max_length=50, default='🏛️')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Destination(models.Model):
    BUDGET_CHOICES = [
        ('free', 'Free'),
        ('budget', 'Budget (< LKR 500)'),
        ('moderate', 'Moderate (LKR 500–2000)'),
        ('premium', 'Premium (LKR 2000+)'),
    ]
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('challenging', 'Challenging'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='destinations')
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, related_name='destinations')
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    
    # Location
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=100, blank=True)
    
    # Media
    featured_image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    
    # Info
    budget_level = models.CharField(max_length=20, choices=BUDGET_CHOICES, default='moderate')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='easy')
    best_time_to_visit = models.CharField(max_length=200, blank=True)
    opening_hours = models.CharField(max_length=200, blank=True)
    entry_fee = models.CharField(max_length=100, blank=True)
    
    # Dress code for religious sites
    requires_dress_code = models.BooleanField(default=False)
    dress_code_description = models.TextField(blank=True)
    
    # Hidden gem flag
    is_hidden_gem = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Safety
    safety_notes = models.TextField(blank=True)
    
    # Tags
    tags = models.CharField(max_length=300, blank=True, help_text='Comma-separated tags')
    
    # Stats
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', '-view_count', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_tags_list(self):
        if self.tags:
            return [t.strip() for t in self.tags.split(',')]
        return []

    def average_rating(self):
        reviews = self.reviews.filter(is_approved=True)
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 1)
        return 0

    def review_count(self):
        return self.reviews.filter(is_approved=True).count()

    def __str__(self):
        return self.name


class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='destinations/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.destination.name} - Image {self.order}"


class FavouriteDestination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='favourited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'destination')
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.user.username} → {self.destination.name}"
