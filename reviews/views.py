from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from destinations.models import Destination
from .models import Review
from .forms import ReviewForm


@login_required
def submit_review(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    existing = Review.objects.filter(user=request.user, destination=destination).first()

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=existing)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.destination = destination
            review.save()
            messages.success(request, 'Your review has been submitted!')
            return redirect('destinations:detail', slug=slug)
    else:
        form = ReviewForm(instance=existing)

    return render(request, 'reviews/submit.html', {
        'form': form,
        'destination': destination,
        'existing': existing,
    })


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    slug = review.destination.slug
    review.delete()
    messages.success(request, 'Review deleted.')
    return redirect('destinations:detail', slug=slug)
