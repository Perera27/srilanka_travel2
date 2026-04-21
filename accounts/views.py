from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, UserProfileForm, UserUpdateForm
from destinations.models import FavouriteDestination
from reviews.models import Review


def register(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Lanka Explorer, {user.first_name}! 🇱🇰')
            return redirect('accounts:setup_profile')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            next_url = request.GET.get('next', 'core:home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('core:home')


@login_required
def setup_profile(request):
    """Initial profile setup after registration."""
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile set up! Now explore Sri Lanka 🌴')
            return redirect('recommendations:get_recommendations')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/setup_profile.html', {'form': form})


@login_required
def profile(request):
    """View and edit user profile."""
    user = request.user
    profile = user.profile
    user_form = UserUpdateForm(instance=user)
    profile_form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')

    favourites = FavouriteDestination.objects.filter(user=user).select_related('destination')[:6]
    my_reviews = Review.objects.filter(user=user).select_related('destination')[:5]

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'favourites': favourites,
        'my_reviews': my_reviews,
    }
    return render(request, 'accounts/profile.html', context)
