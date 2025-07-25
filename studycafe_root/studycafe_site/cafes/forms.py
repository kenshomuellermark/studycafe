from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Cafe, CafePhoto

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']



class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = [
            'name', 'address', 'description', 'photo',
            'has_wifi', 'has_power_outlet', 'has_restroom',
            'opening_time', 'closing_time',
            'latitude', 'longitude'
        ]
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'opening_time': forms.TimeInput(attrs={'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class CafePhotoForm(forms.ModelForm):
    class Meta:
        model = CafePhoto
        fields = ['image', 'caption']
        widgets = {
            'caption': forms.TextInput(attrs={'placeholder': 'Add a caption (optional)'})
        }