"""artsite URL Configuration
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from home import views
from .views import about, contact
from accounts.views import login, logout, register, profile
from django.conf import settings 
from gallery.views import edit_profile
from artwork.views import productsall, productdetail, checkout
from basket.views import view_basket, add_to_basket, adjust_basket


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.index, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),

    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),

    url(r'^profile/$', profile, name='profile'),
    url(r'^edit_profile/$', edit_profile, name='edit_profile'),

    url(r'^products/', include('artwork.urls')),
    url(r'^basket/', include('basket.urls')),

    url(r'^pages/', include('django.contrib.flatpages.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

