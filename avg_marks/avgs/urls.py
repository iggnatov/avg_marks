from django.urls import path, re_path

from .views import AppRate, AppStat

urlpatterns = [
    re_path('api/rate+', AppRate.as_view()),
    re_path('api/stat+', AppStat.as_view()),
]
