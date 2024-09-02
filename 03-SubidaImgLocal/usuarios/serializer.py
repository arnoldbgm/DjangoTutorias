from rest_framework import serializers
from .models import CustomUser

class CustomUserSerailizer(serializers.ModelSerializer):

   # Validar
   # Deserealizar el JSON y convertilo en un formato de pueda ser usado en Python
   # Insertar la data que se envia
   # Responder 

   # Para enviar el password y que este no sea devuelto en la respuesta de Django
   password = serializers.CharField(write_only = True, required = True)

   class Meta:
      model = CustomUser
      fields = ['username', 'password', 'imagen', 'dni', 'telefono']

   def create(self, validated_data):
      # Primero va ir mi tabla
      user = CustomUser.objects.create_user(
         username=validated_data['username'],
         password=validated_data['password'],
         imagen=validated_data.get('imagen', None),
         dni=validated_data.get('dni', None),
         telefono=validated_data.get('telefono', None)
      )
      return user
