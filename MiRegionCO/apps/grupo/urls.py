from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login_view, name='login'),
    url(r'^logout$', logout_view, name='logout')
]
