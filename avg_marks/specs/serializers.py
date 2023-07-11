from rest_framework import serializers

from specs.models import Spec


class SpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spec
        fields = ['code', 'spec_name']