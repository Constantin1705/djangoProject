from django import forms
from django.forms import TextInput, EmailInput, Textarea, DateTimeInput, DateInput, Select

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'  # formularul va contine toate field-urile din modelul Student(models.py)
        fields = ['first_name', 'last_name', 'age', 'is_olympic',
                  'email', 'description', 'start_date', 'end_date',
                  'average', 'gender', 'professor']  # putem schimba si ordinea field-urilor

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control'}),
            'age': TextInput(attrs={'placeholder': 'Enter your age', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Enter your description', 'class': 'form-control'}),
            'start_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'average': TextInput(attrs={'placeholder': 'Enter your average', 'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'professor': Select(attrs={'class': 'form-control'})
        }