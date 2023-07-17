from django.urls import path, re_path
from rest_framework import routers

from . import views
from .views import AppRate

urlpatterns = [
    #path('', views.index, name='index'),
    re_path('api/avgs+', AppRate.as_view())
]
