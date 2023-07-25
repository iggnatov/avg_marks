from decimal import *

from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView

from specs.models import Spec
from .models import Application


class AppRate(APIView):
    def get(self, request):
        code = self.request.query_params.get('spec_code')
        mark = self.request.query_params.get('mark')
        grade = self.request.query_params.get('grade')

        # correcting values
        delta = 0.43

        c_mark = round((float(mark) + delta), 2)
        str(c_mark)

        queryset = Application.objects.filter(spec_code=code).filter(grade=grade).filter(avg_marks__gte=c_mark)
        rate_mos = len(queryset) + 1
        rate_originals = len(queryset.filter(originals=True)) + 1
        response = {
            'spec_code': code,
            'mark': mark,
            'rate_mos': rate_mos,
            'rate_originals': rate_originals,
            'grade': grade
        }
        return Response(response)


class AppStat(APIView):
    @staticmethod
    def get(request):
        def get_spec_codes(_grade):
            if _grade:
                specs = Spec.objects.filter(after_09=True)
            else:
                specs = Spec.objects.filter(after_11=True)
            spec_codes = []
            for i in range(len(specs)):
                spec_codes.append(specs[i].code)
            return spec_codes

        grade = [True, False]
        response = {}

        for grade_status in grade:
            response[f'response{grade_status}'] = {}
            all_spec_codes = get_spec_codes(grade_status)
            for code in all_spec_codes:
                queryset = Application.objects.filter(grade=grade_status).filter(spec_code=code)
                response[f'response{grade_status}']['r_qty_mos_' + code.replace('.', '')] = queryset.count()
                response[f'response{grade_status}']['r_qty_originals_' + code.replace('.', '')] = \
                    queryset.filter(originals=True).count()
                response[f'response{grade_status}']['r_avg_marks_' + code.replace('.', '')] = \
                    queryset.aggregate(Avg('avg_marks'))['avg_marks__avg'].quantize(Decimal('0.01'))
                r_avg_marks_originals_ = queryset.filter(originals=True).aggregate(Avg('avg_marks'))['avg_marks__avg'] \
                    .quantize(Decimal('0.01')) - Decimal(0.43)
                response[f'response{grade_status}']['r_avg_marks_originals_' + code.replace('.', '')] = \
                    r_avg_marks_originals_

        return Response(response)
