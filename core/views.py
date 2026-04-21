from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Count
from destinations.models import Destination, Category
from reviews.models import Review


def home(request):
    featured = Destination.objects.filter(is_featured=True, is_active=True).select_related('category', 'province')[:6]
    hidden_gems = Destination.objects.filter(is_hidden_gem=True, is_active=True).order_by('?')[:4]
    categories = Category.objects.all()
    popular = Destination.objects.filter(is_active=True).order_by('-view_count')[:8]
    total_destinations = Destination.objects.filter(is_active=True).count()

    context = {
        'featured': featured,
        'hidden_gems': hidden_gems,
        'categories': categories,
        'popular': popular,
        'total_destinations': total_destinations,
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def safety_tips(request):
    return render(request, 'core/safety.html')


def is_manager_or_admin(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_manager_or_admin)
def manager_dashboard(request):
    latest_reviews = Review.objects.select_related('user', 'destination').order_by('-created_at')[:8]
    top_destinations = Destination.objects.filter(is_active=True).annotate(
        review_total=Count('reviews')
    ).order_by('-view_count', 'name')[:5]

    context = {
        'total_destinations': Destination.objects.count(),
        'active_destinations': Destination.objects.filter(is_active=True).count(),
        'hidden_gems_count': Destination.objects.filter(is_hidden_gem=True, is_active=True).count(),
        'total_reviews': Review.objects.count(),
        'pending_reviews': Review.objects.filter(is_approved=False).count(),
        'total_users': User.objects.count(),
        'latest_reviews': latest_reviews,
        'top_destinations': top_destinations,
        'is_administrator': request.user.is_superuser,
    }
    return render(request, 'core/manager_dashboard.html', context)