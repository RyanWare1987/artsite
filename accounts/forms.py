from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    """
    The Form a user is presented with when signing up
    for a new account. A user is asked to supply an email 
    address, username, and password with a confirmation 
    checker in place.
    """
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        """
        Here we are checking if the input in password1 and
        password2 match, if they do not we throw an error
        """
        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)



class UserLoginForm(forms.Form):
    """
    Simple login form presented to the user. We
    only ask for the Email Address linked to the
    account and a password.
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

