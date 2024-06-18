from rest_framework import serializers
from .models import StudenInfo
class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=StudenInfo
        fields='__all__'