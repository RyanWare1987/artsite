from django import forms
from .models import Profile

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
            'instagram_url',
            'linkedin_url',
            'youtube_url',
            'pintrest_url'
        )
