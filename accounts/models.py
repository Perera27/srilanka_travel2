from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    TRAVELLER_TYPE_CHOICES = [
        ('domestic', 'Domestic Traveller'),
        ('international', 'International Traveller'),
    ]
    INTEREST_CHOICES = [
        ('beach', 'Beach & Coastal'),
        ('wildlife', 'Wildlife & Nature'),
        ('cultural', 'Cultural & Heritage'),
        ('religious', 'Religious & Spiritual'),
        ('adventure', 'Adventure & Trekking'),
        ('historical', 'Historical Sites'),
        ('food', 'Food & Cuisine'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    traveller_type = models.CharField(max_length=20, choices=TRAVELLER_TYPE_CHOICES, default='domestic')
    nationality = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    # Preferences for recommendations
    preferred_budget = models.CharField(max_length=20, blank=True)
    preferred_difficulty = models.CharField(max_length=20, blank=True)
    interests = models.CharField(max_length=500, blank=True, help_text='Comma-separated interests')
    
    # Current location (optional)
    current_province = models.CharField(max_length=100, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_interests_list(self):
        if self.interests:
            return [i.strip() for i in self.interests.split(',')]
        return []

    def __str__(self):
        return f"{self.user.username}'s Profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
