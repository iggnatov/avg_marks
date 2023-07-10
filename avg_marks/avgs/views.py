from django.shortcuts import render
from .models import Application


def index(request):

    apps = Application.objects.filter()

    context = {
        'apps': apps
    }

    return render(request, 'index.html', context)
