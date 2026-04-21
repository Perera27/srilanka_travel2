from destinations.models import Destination
from django.db.models import Q


def get_recommendations_for_user(user, limit=12):
    """
    Personalised recommendation engine based on:
    1. User's stated interest categories
    2. Preferred budget level
    3. Preferred difficulty
    4. Nearby province (if set)
    Excludes already-favourited destinations.
    Falls back to featured/popular destinations.
    """
    profile = user.profile
    favourited_ids = user.favourites.values_list('destination_id', flat=True)

    qs = Destination.objects.filter(is_active=True).exclude(id__in=favourited_ids)

    scored = []
    interests = profile.get_interests_list()

    for dest in qs.select_related('category', 'province'):
        score = 0
        # Interest match
        if dest.category and dest.category.category_type in interests:
            score += 3
        # Budget match
        if profile.preferred_budget and dest.budget_level == profile.preferred_budget:
            score += 2
        # Difficulty match
        if profile.preferred_difficulty and dest.difficulty == profile.preferred_difficulty:
            score += 2
        # Province proximity
        if profile.current_province and dest.province:
            if profile.current_province.lower() in dest.province.name.lower():
                score += 4
        # Featured boost
        if dest.is_featured:
            score += 1
        # Popularity
        score += min(dest.view_count // 100, 3)

        scored.append((score, dest))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for _, d in scored[:limit]]


def get_similar_destinations(destination, limit=4):
    """Return destinations similar to a given one (same category, nearby province)."""
    return Destination.objects.filter(
        Q(category=destination.category) | Q(province=destination.province),
        is_active=True
    ).exclude(id=destination.id).order_by('-is_featured', '-view_count')[:limit]
