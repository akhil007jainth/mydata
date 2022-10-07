from dataclasses import field
from rest_framework import serializers
from .models import  signup
class signup_serializers(serializers.ModelSerializer):
    # name=serializers.CharField(max_length=100)
    # email=serializers.EmailField(max_length=100)
    # username=serializers.CharField(max_length=100)
    # password=serializers.CharField(max_length=50)
    class Meta:
        model=signup
        fields='__all__'