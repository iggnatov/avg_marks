from django.urls import path
from rest_framework import routers

from . import views
from .views import SpecViewSet

router = routers.SimpleRouter()
router.register('api/specs', SpecViewSet)

urlpatterns = [
    path('', views.get_specs, name='specs')
]

urlpatterns += router.urls
