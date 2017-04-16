from django.conf.urls import url
from django.contrib import admin
from .views import homepage, upload, detectemotion

urlpatterns = [
    url(r'^$',homepage, name="homepage" ),
    url(r'^upload/$',upload, name="upload" ),
    url(r'^detectemotion/$',detectemotion, name="detectemotion" ),
]


