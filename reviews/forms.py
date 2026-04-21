from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)]
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'star-radio'}),
    )

    class Meta:
        model = Review
        fields = ['rating', 'title', 'content', 'visit_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Summarise your experience'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Share your experience...'}),
            'visit_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
