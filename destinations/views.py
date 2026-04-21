from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed
from django.db.models import Q, Avg
from django.contrib import messages
from .models import Destination, Category, Province, FavouriteDestination
from reviews.models import Review


def destination_list(request):
    """Browse all destinations with filters."""
    destinations = Destination.objects.filter(is_active=True).select_related('category', 'province')
    categories = Category.objects.all()
    provinces = Province.objects.all()

    # Filters
    category_slug = request.GET.get('category', '')
    province_slug = request.GET.get('province', '')
    budget = request.GET.get('budget', '')
    difficulty = request.GET.get('difficulty', '')
    hidden_gem = request.GET.get('hidden_gem', '')
    search_q = request.GET.get('q', '')

    if category_slug:
        destinations = destinations.filter(category__slug=category_slug)
    if province_slug:
        destinations = destinations.filter(province__slug=province_slug)
    if budget:
        destinations = destinations.filter(budget_level=budget)
    if difficulty:
        destinations = destinations.filter(difficulty=difficulty)
    if hidden_gem:
        destinations = destinations.filter(is_hidden_gem=True)
    if search_q:
        destinations = destinations.filter(
            Q(name__icontains=search_q) |
            Q(description__icontains=search_q) |
            Q(city__icontains=search_q) |
            Q(tags__icontains=search_q)
        )

    context = {
        'destinations': destinations,
        'categories': categories,
        'provinces': provinces,
        'selected_category': category_slug,
        'selected_province': province_slug,
        'selected_budget': budget,
        'selected_difficulty': difficulty,
        'search_q': search_q,
        'hidden_gem': hidden_gem,
        'budget_choices': Destination.BUDGET_CHOICES,
        'difficulty_choices': Destination.DIFFICULTY_CHOICES,
    }
    return render(request, 'destinations/list.html', context)


def destination_detail(request, slug):
    """Detailed view of a single destination."""
    destination = get_object_or_404(Destination, slug=slug, is_active=True)
    destination.view_count += 1
    destination.save(update_fields=['view_count'])

    if request.user.is_authenticated:
        try:
            from recommendations.models import TravelHistory
            TravelHistory.objects.update_or_create(
                user=request.user,
                destination=destination,
                defaults={'visited': False},
            )
        except Exception:
            pass

    reviews = destination.reviews.filter(is_approved=True).order_by('-created_at')
    images = destination.images.all()
    
    # Related destinations (same category)
    related = Destination.objects.filter(
        category=destination.category, is_active=True
    ).exclude(id=destination.id)[:4]

    is_favourite = False
    if request.user.is_authenticated:
        is_favourite = FavouriteDestination.objects.filter(
            user=request.user, destination=destination
        ).exists()

    context = {
        'destination': destination,
        'reviews': reviews,
        'images': images,
        'related': related,
        'is_favourite': is_favourite,
    }
    return render(request, 'destinations/detail.html', context)


@login_required
def toggle_favourite(request, slug):
    """AJAX toggle favourite destination."""
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    destination = get_object_or_404(Destination, slug=slug, is_active=True)
    fav, created = FavouriteDestination.objects.get_or_create(
        user=request.user, destination=destination
    )
    if not created:
        fav.delete()
        return JsonResponse({'status': 'removed', 'message': 'Removed from favourites'})
    return JsonResponse({'status': 'added', 'message': 'Added to favourites'})


@login_required
def my_favourites(request):
    """User's saved/favourite destinations."""
    favourites = FavouriteDestination.objects.filter(
        user=request.user
    ).select_related('destination', 'destination__category')
    return render(request, 'destinations/favourites.html', {'favourites': favourites})


def hidden_gems(request):
    """Showcase lesser-known destinations."""
    gems = Destination.objects.filter(is_hidden_gem=True, is_active=True).select_related('category', 'province')
    return render(request, 'destinations/hidden_gems.html', {'gems': gems})
