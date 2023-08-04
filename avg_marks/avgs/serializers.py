from rest_framework import serializers

from avgs.models import Application, AppRQty


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['spec_code', 'financing_type', 'originals', 'avg_marks', 'grade']


class AppRQtySerializer(serializers.ModelSerializer):
    class Meta:
        model = AppRQty
        fields = ['today', 'day', 'q_ty']

