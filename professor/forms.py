from django import forms
from django.forms import TextInput, Select, TimeInput

from professor.models import Professor


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor

        fields = ['first_name', 'last_name', 'department', 'time']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Enter your last_name', 'class': 'form-control'}),
            'department': Select(attrs={'class': 'form-control'}),
            'time': TimeInput(attrs={'class': 'form-control', 'type': 'time'})
        }