# dataset/serializers.py
from rest_framework import serializers
from dataset.models import Dataset

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'
