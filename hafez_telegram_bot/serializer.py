from rest_framework import serializers
from .models import Hafez_Fall


class HafezFallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hafez_Fall
        fields = 'id', 'text', 'description',
