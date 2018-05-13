from django.conf.urls import url
import views

urlpatterns = [
    
    url(r'^$', views.image_list, name="image_list"),
    url(r'^/$', views.image_list, name="image_list"),
    url(r'^(?P<id>\d+)/$', views.image_detail),
    url(r'^post/$', views.new_image, name='new_image'),

]