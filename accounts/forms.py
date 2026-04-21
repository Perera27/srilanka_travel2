from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class UserProfileForm(forms.ModelForm):
    INTEREST_CHOICES = [
        ('beach', 'Beach & Coastal'),
        ('wildlife', 'Wildlife & Nature'),
        ('cultural', 'Cultural & Heritage'),
        ('religious', 'Religious & Spiritual'),
        ('adventure', 'Adventure & Trekking'),
        ('historical', 'Historical Sites'),
        ('food', 'Food & Cuisine'),
    ]
    
    interests_select = forms.MultipleChoiceField(
        choices=INTEREST_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Your Travel Interests'
    )

    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'traveller_type', 'nationality', 'phone',
                  'preferred_budget', 'preferred_difficulty', 'current_province']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'traveller_type': forms.Select(attrs={'class': 'form-select'}),
            'preferred_budget': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('', 'No preference'), ('free', 'Free'), ('budget', 'Budget'),
                ('moderate', 'Moderate'), ('premium', 'Premium')
            ]),
            'preferred_difficulty': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('', 'No preference'), ('easy', 'Easy'), ('moderate', 'Moderate'), ('challenging', 'Challenging')
            ]),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'current_province': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.interests:
            self.fields['interests_select'].initial = self.instance.get_interests_list()

    def save(self, commit=True):
        profile = super().save(commit=False)
        interests = self.cleaned_data.get('interests_select', [])
        profile.interests = ','.join(interests)
        if commit:
            profile.save()
        return profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
