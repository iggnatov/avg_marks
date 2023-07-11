from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from avgs.models import Application
from .models import Spec
from .serializers import SpecSerializer


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


class SpecViewSet(viewsets.ModelViewSet):
    queryset = Spec.objects.all().order_by("code")
    serializer_class = SpecSerializer


# class SpecList(APIView):
#     def get(self, request):
#         queryset = Spec.objects.all().order_by("code")
#
#
#         return Response()