from django.shortcuts import render

from avgs.models import Application
from .models import Spec


def get_specs(request):

    specs = Spec.objects.all().order_by("code")

    vals = {}
    for spec in specs:
        vals[spec.code] = len(Application.objects.filter(spec_code=spec.code))
        # print(vals[spec.code])


    context = {
        'specs': specs,
        'vals': vals
    }

    return render(request, 'specs.html', context)
