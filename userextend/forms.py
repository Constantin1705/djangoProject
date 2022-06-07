from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class UserExtendForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter last name', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Please enter user name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Please enter email', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserExtendForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Please enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Please enter your password confirmation'