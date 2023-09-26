from django import forms
from .models import Distros, Features, Machines
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class DistrosForm(forms.ModelForm):
    launch_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}))

    class Meta:
        model = Distros
        fields = ['name', 'available', 'processor', 'launch_date']


class MachinesForm(forms.ModelForm):
    launch_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}))

    class Meta:
        model = Machines
        fields = ['name', 'available', 'processor', 'launch_date']


class FeaturesForm(forms.ModelForm):
    launch_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}))

    class Meta:
        model = Features
        fields = ['name', 'status', 'version', 'launch_date']


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email"]
