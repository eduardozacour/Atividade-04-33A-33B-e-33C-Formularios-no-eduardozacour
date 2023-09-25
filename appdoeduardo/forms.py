from django import forms
from .models import Distros, Features, Machines


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
