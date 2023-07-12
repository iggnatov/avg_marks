from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView

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
    serializer_class = AppSerializer

    queryset = Application.objects.filter(spec_code="09.02.07") \
        .order_by("avg_marks") \
        .filter(avg_marks__gte=4.2) \
        .filter(originals=True)


class AppRate(APIView):
    def get(self, request):
        code = self.request.query_params.get('spec_code')
        mark = self.request.query_params.get('mark')
        queryset = Application.objects.filter(spec_code=code).filter(avg_marks__gte=mark)
        rate_mos = len(queryset.filter(originals=False)) + 1
        rate_originals = len(queryset.filter(originals=True)) + 1
        response = {
            'spec_code': code,
            'mark': mark,
            'rate_mos': rate_mos,
            'rate_originals': rate_originals
        }
        return Response(response)

# class AppList(generics.ListAPIView):
#     serializer_class = AppSerializer
#
#     def get_queryset(self):
#         queryset = Application.objects.all()
#         code = self.request.query_params.get('spec_code')
#         mark = self.request.query_params.get('mark')
#         if code is not None:
#             queryset = queryset.filter(spec_code=code).filter(avg_marks__gte=mark)
#             print(type(queryset[0]))
#         return queryset
