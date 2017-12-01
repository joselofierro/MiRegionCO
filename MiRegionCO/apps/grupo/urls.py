from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', login_view, name='index'),
    url(r'^logout$', logout_view, name='logout')
]
