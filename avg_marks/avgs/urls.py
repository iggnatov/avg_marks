from django.urls import path, re_path

from . import views
from .views import AppRate, AppStat, AdminStat

urlpatterns = [
    re_path('api/rate+', AppRate.as_view()),
    re_path('api/stat+', AppStat.as_view()),
    re_path('api/adminstat+', AdminStat.as_view()),
    re_path('api/allstat+', views.index)
]
