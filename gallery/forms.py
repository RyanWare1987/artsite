from django import forms
from .models import Image, Profile, Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = (
            'title',
            'description',
            'tags'
        )


class ImagePostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = (
            'title',
            'description',
            'tags',
            'image'
        )

class ProfileEditForm(forms.ModelForm):
    # Edit profile details - this is for the additional Profile data
    # Which does not involve sensitive information like emails and pw
    class Meta:
        model = Profile
        fields = (
            'name',
            'date_of_birth',
            'fav_artist',
            'occupation',
            'medium',
            'website',
            'about_me',
            'facebook_url',
            'twitter_url',
            'instagram_url'
        )