from django.db import models
from django.contrib.auth.models import User


class TravelHistory(models.Model):
    """Track destinations a user has visited or viewed."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='travel_history')
    destination = models.ForeignKey('destinations.Destination', on_delete=models.CASCADE)
    visited = models.BooleanField(default=False)
    viewed_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'destination')
        ordering = ['-viewed_at']

    def __str__(self):
        return f"{self.user.username} → {self.destination.name}"
