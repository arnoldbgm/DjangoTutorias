from rest_framework import serializers
from .models import GeneroModel

class GeneroSerializer(serializers.ModelSerializer):
   class Meta:
      model = GeneroModel
      fields = '__all__'