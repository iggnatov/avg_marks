from decimal import *

from django.db.models import Avg, Sum
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from specs.models import Spec
from .models import Application, AppRQty


class AppRate(APIView):
    def get(self, request):
        code = self.request.query_params.get('spec_code')
        mark = self.request.query_params.get('mark')
        grade = self.request.query_params.get('grade')

        delta = 0.36
        # correcting values
        if code == "54.01.20":
            delta = 0
        elif grade == "False" and (code == "09.02.07" or code == "09.02.06" or code == "10.02.05"):
            delta = 0.15
        elif grade == "True" and (code == "09.02.07" or code == "09.02.06" or code == "10.02.05"):
            delta = 0
        elif grade == "True" and (code == "13.02.11" or code == "09.02.01"):
            delta = 0.15
        else:
            delta = 0.36

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
            grader = '09' if grade_status else '11'
            response[f'response{grader}'] = {}
            all_spec_codes = get_spec_codes(grade_status)  # get the list of spec_codes for 09 and 11

            for code in all_spec_codes:

                coder = 'spec_' + code.replace('.', '')
                response[f'response{grader}'][f'{coder}'] = {}
                queryset = Application.objects.filter(grade=grade_status).filter(spec_code=code)

                if grade_status:
                    spec_queryset = Spec.objects.filter(after_09=True).filter(code=code)
                    plan_priema_ = spec_queryset[0].plan_priema_09

                    # убираем поправочный коэффициент у специальностей, набравших почти 100%
                    if code == "09.02.07" or code == "09.02.06" or code == "54.01.20" or code == "10.02.05":
                        delta = 0
                    elif code == "09.02.01" or code == "13.02.11":
                        delta = 0.15
                    else:
                        delta = 0.36

                else:
                    spec_queryset = Spec.objects.filter(after_11=True).filter(code=code)
                    plan_priema_ = spec_queryset[0].plan_priema_11

                    # убираем поправочный коэффициент у специальностей, набравших почти 100%
                    if code == "54.01.20":
                        delta = 0
                    else:
                        delta = 0.15

                # Код
                response[f'response{grader}'][f'{coder}']['r_code_'] = spec_queryset[0].code

                # Специальность
                response[f'response{grader}'][f'{coder}']['r_spec_name_'] = spec_queryset[0].spec_name

                # Корпус обучения
                response[f'response{grader}'][f'{coder}']['r_address_'] = spec_queryset[0].address

                # Срок обучения
                response[f'response{grader}'][f'{coder}']['r_period_of_study_'] = spec_queryset[0].period_of_study_09

                # План приема
                response[f'response{grader}'][f'{coder}']['r_plan_priema_'] = plan_priema_

                # Количество поданных заявлений через портал mos.ru
                response[f'response{grader}'][f'{coder}']['r_qty_mos_'] = queryset.count()

                # Средний балл по заявлениям
                response[f'response{grader}'][f'{coder}']['r_avg_marks_'] = \
                    queryset.aggregate(Avg('avg_marks'))['avg_marks__avg'].quantize(Decimal('0.01'))

                # Количество человек, сдавших оригиналы
                response[f'response{grader}'][f'{coder}']['r_qty_originals_'] = \
                    queryset.filter(originals=True).count()

                # Средний балл по оригиналам
                r_avg_marks_originals_ = queryset.filter(originals=True).aggregate(Avg('avg_marks'))['avg_marks__avg'] \
                    .quantize(Decimal('0.01')) - Decimal(delta)
                response[f'response{grader}'][f'{coder}']['r_avg_marks_originals_'] = \
                    r_avg_marks_originals_.quantize(Decimal('0.01'))

        return Response(response)


def index(request):
    def get_spec_codes(_grade):
        spec_queryset_ = Spec.objects.all()
        if _grade:
            specs = spec_queryset_.filter(after_09=True)
        else:
            specs = spec_queryset_.filter(after_11=True)
        spec_codes = []
        for i in range(len(specs)):
            spec_codes.append(specs[i].code)
        return spec_codes

    grade = [True, False]
    response = {}

    for grade_status in grade:
        grader = '09' if grade_status else '11'
        response[f'response{grader}'] = {}
        all_spec_codes = get_spec_codes(grade_status)  # get the list of spec_codes for 09 and 11

        for code in all_spec_codes:
            coder = 'spec_' + code.replace('.', '')
            response[f'response{grader}'][f'{coder}'] = {}
            queryset = Application.objects.filter(grade=grade_status).filter(spec_code=code)
            if grade_status:
                spec_queryset = Spec.objects.filter(after_09=True).filter(code=code)
                plan_priema_ = spec_queryset[0].plan_priema_09

                # убираем поправочный коэффициент у специальностей, набравших почти 100%
                if code == "09.02.07" or code == "09.02.06" or code == "54.01.20" or code == "10.02.05":
                    delta = 0
                elif code == "09.02.01" or code == "13.02.11":
                    delta = 0.15
                else:
                    delta = 0.36

            else:
                spec_queryset = Spec.objects.filter(after_11=True).filter(code=code)
                plan_priema_ = spec_queryset[0].plan_priema_11

                # убираем поправочный коэффициент у специальностей, набравших почти 100%
                if code == "54.01.20":
                    delta = 0
                else:
                    delta = 0.15

            # Код
            response[f'response{grader}'][f'{coder}']['r_code_'] = spec_queryset[0].code

            # Специальность
            response[f'response{grader}'][f'{coder}']['r_spec_name_'] = spec_queryset[0].spec_name

            # Корпус обучения
            response[f'response{grader}'][f'{coder}']['r_address_'] = spec_queryset[0].address

            # Срок обучения
            if grader == '09':
                response[f'response{grader}'][f'{coder}']['r_period_of_study_'] = spec_queryset[0].period_of_study_09
            else:
                response[f'response{grader}'][f'{coder}']['r_period_of_study_'] = spec_queryset[0].period_of_study_11

            # План приема
            response[f'response{grader}'][f'{coder}']['r_plan_priema_'] = plan_priema_

            # Количество поданных заявлений через портал mos.ru
            response[f'response{grader}'][f'{coder}']['r_qty_mos_'] = queryset.count()

            # Средний балл по заявлениям
            # response[f'response{grader}'][f'{coder}']['r_avg_marks_'] = \
            #     queryset.aggregate(Avg('avg_marks'))['avg_marks__avg'].quantize(Decimal('0.01'))

            # Количество человек, сдавших оригиналы
            response[f'response{grader}'][f'{coder}']['r_qty_originals_'] = \
                queryset.filter(originals=True).count()

            # Средний балл по оригиналам
            r_avg_marks_originals_ = queryset.filter(originals=True).aggregate(Avg('avg_marks'))['avg_marks__avg'] \
                .quantize(Decimal('0.01')) - Decimal(delta)
            response[f'response{grader}'][f'{coder}']['r_avg_marks_originals_'] = \
                r_avg_marks_originals_.quantize(Decimal('0.01'))

    return render(request, 'index.html', {'response': response})


class AdminStat(APIView):

    def get(self, request):
        queryset = Application.objects.all()
        qty_mos = len(queryset)
        qty_mos_130211 = len(queryset.filter(spec_code="13.02.11"))
        qty_mos_130114 = len(queryset.filter(spec_code="13.01.14"))
        qty_originals = len(queryset.filter(originals="True"))
        qty_oroginals_130211 = len(queryset.filter(originals=True).filter(spec_code="13.02.11"))
        qty_originals_130114 = len(queryset.filter(originals=True).filter(spec_code="13.01.14"))

        rqty = AppRQty.objects.all().order_by('day')
        rqty_qty = rqty.aggregate(Sum('q_ty'))['q_ty__sum']

        rqty_response = {}
        for elem in rqty:
            rqty_response[f'{elem.day}'] = elem.q_ty
        rqty_response_str = ''
        for k, v in rqty_response.items():
            rqty_response_str += f'{k}: {v} <br />'

        response = {
            "qty_mos": qty_mos,
            "qty_mos_130211": qty_mos_130211,
            "qty_mos_130114": qty_mos_130114,
            "qty_originals": qty_originals,
            "qty_oroginals_130211": qty_oroginals_130211,
            "qty_originals_130114": qty_originals_130114,
            "rqty_qty": rqty_qty,
            "rqty_response": rqty_response_str,
        }

        return Response(response)
