from django.conf.urls import url
from django.conf import settings
import views
from .views import edit_profile

urlpatterns = [
    
    url(r'^$', views.image_list, name="image_list"),
    url(r'^/$', views.image_list, name="image_list"),
    url(r'^(?P<id>\d+)/$', views.image_detail),
    url(r'^post/$', views.new_image, name='new_image'),

    url(r'^edit_profile/$', edit_profile, name='edit_profile'),

]
