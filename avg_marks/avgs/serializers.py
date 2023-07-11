from rest_framework import serializers

from avgs.models import Application


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['spec_code', 'financing_type', 'originals', 'avg_marks']

