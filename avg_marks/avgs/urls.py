from django.urls import path
from rest_framework import routers

from . import views
from .views import AppViewSet

router = routers.SimpleRouter()
router.register('api/avgs', AppViewSet)

urlpatterns = [
    path('', views.index, name='index')
]

urlpatterns += router.urls
