from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from destinations.models import Destination
from .engine import get_recommendations_for_user


@login_required
def get_recommendations(request):
    """Show personalised travel recommendations."""
    recommendations = get_recommendations_for_user(request.user)
    profile = request.user.profile

    context = {
        'recommendations': recommendations,
        'profile': profile,
        'interests': profile.get_interests_list(),
    }
    return render(request, 'recommendations/recommendations.html', context)


def popular_destinations(request):
    """Public page: popular / trending destinations."""
    popular = Destination.objects.filter(is_active=True).order_by('-view_count')[:12]
    featured = Destination.objects.filter(is_featured=True, is_active=True)[:6]
    return render(request, 'recommendations/popular.html', {
        'popular': popular,
        'featured': featured,
    })
