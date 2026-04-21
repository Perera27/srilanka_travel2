from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    destination = models.ForeignKey(
        'destinations.Destination', on_delete=models.CASCADE, related_name='reviews'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    visit_date = models.DateField(null=True, blank=True)
    is_approved = models.BooleanField(default=True)  # Admin can moderate
    helpful_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('destination', 'user')
        ordering = ['-created_at']

    def get_stars(self):
        return range(self.rating)

    def get_empty_stars(self):
        return range(5 - self.rating)

    def __str__(self):
        return f"{self.user.username} → {self.destination.name} ({self.rating}★)"
