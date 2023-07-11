from django.shortcuts import render
from rest_framework import viewsets

from .models import Application
from .serializers import AppSerializer


def index(request):
    apps = Application.objects.filter(spec_code="09.02.07")\
        .order_by("avg_marks")\
        .filter(avg_marks__gte=4.2)\
        .filter(originals=True)

    rate = len(apps)

    context = {
        'apps': apps,
        'rate': rate
    }

    return render(request, 'index.html', context)


class AppViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.filter(spec_code="09.02.07")\
        .order_by("avg_marks")\
        .filter(avg_marks__gte=4.2)\
        .filter(originals=True)

    serializer_class = AppSerializer
