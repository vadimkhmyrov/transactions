from __future__ import unicode_literals
from django.conf.urls import url, include
from . import views

app_name = 'billing'

urlpatterns = [
    url(r'^$', views.main_view, name='index'),
]
