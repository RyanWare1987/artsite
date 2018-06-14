"""artsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from home import views
from .views import about, contact
from accounts.views import login, logout, register, profile, image_form_upload
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
    url(r'^image_form_upload/$', image_form_upload, name='image_form_upload'),
    #url(r'^products/(?P<id>\d+)/$', productdetail),
    #url(r'^products/$', productsall, name='products'),

    url(r'^products/', include('artwork.urls')),

    url(r'^basket/', include('basket.urls')),


    url(r'^pages/', include('django.contrib.flatpages.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#if settings.DEBUG:
    #urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)) 