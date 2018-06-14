from django.conf.urls import url
from django.conf import settings
import views
from .views import edit_profile

urlpatterns = [

    url(r'^edit_profile/$', edit_profile, name='edit_profile'),

]
