from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Image
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
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

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    #def save(self, commit=True):
       #instance = super(UserRegistrationForm, self).save(commit=False)

        # automatically set to email address to create a unique identifier
        #instance.username = instance.email

        #if commit:
           # instance.save()

        #return instance


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    ### Currently not needed if just going for profile edit form - can have all the junk in there
    # Edit user details - this is for the User model, which contains
    # sensitive info such as email, username, password etc
    class Meta:
        model = User
        fields = (
            'email',
            'username',
        )


class ImageForm(forms.ModelForm):
    class Meta: 
        model = Image
        fields = (
            'description',
            'image'
        )