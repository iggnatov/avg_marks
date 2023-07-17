from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Application


class AppRate(APIView):
    def get(self, request):
        code = self.request.query_params.get('spec_code')
        mark = self.request.query_params.get('mark')
        grade = self.request.query_params.get('grade')
        queryset = Application.objects.filter(spec_code=code).filter(grade=grade).filter(avg_marks__gte=mark)
        rate_mos = len(queryset.filter(originals=False)) + 1
        rate_originals = len(queryset.filter(originals=True)) + 1
        response = {
            'spec_code': code,
            'mark': mark,
            'rate_mos': rate_mos,
            'rate_originals': rate_originals,
            'grade': grade
        }
        return Response(response)
