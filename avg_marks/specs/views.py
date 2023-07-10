from django.shortcuts import render

from .models import Spec


def get_specs(request):

    specs = Spec.objects.filter()

    context = {
        'specs': specs
    }

    return render(request, 'specs.html', context)
