from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput

from home.models import  UserProfile

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username' , 'email', 'first_name', 'last_name')
        widgets = {
            'username'  : TextInput(attrs={'class' : 'input' , 'placeorder' : 'username'}),
            'email'     : TextInput(attrs={'class': 'input', 'placeorder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeorder': 'first_name'}),
            'last_name' : TextInput(attrs={'class': 'input', 'placeorder': 'last_name'}),

        }

CITY = [
    ('Istanbul ', 'Istanbul '),
    ('Ankara ', 'Ankara '),
    ('Izmir ', 'Izmir '),

]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address' , 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeorder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeorder': 'address'}),
            'city': TextInput(attrs={'class': 'input', 'placeorder': 'city'}),
            'country': TextInput(attrs={'class': 'input', 'placeorder': 'country'}),
            'image': TextInput(attrs={'class': 'input', 'placeorder': 'image',}),

        }