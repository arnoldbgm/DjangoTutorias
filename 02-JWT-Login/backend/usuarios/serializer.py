from rest_framework import serializers
# PAra usar la tabla usuarios de Django debo usar la sgte importacion
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

   # Para evitar que se devuelva la contraseña en la respuesta debo usar lo siguiente
   password = serializers.CharField(write_only=True)
   class Meta:
      model = User
      fields = ['username', 'password', 'email', 'first_name', 'last_name']
      #Si yo quiero obligar a DRF a que me exiga algunos campos debo colocar lo siguiente
      extra_kwargs = {
         'username': {'required': True},
         'password': {'required': True},
         'email': {'required': True},
         'first_name': {'required': True},
         'last_name': {'required': True},
      }

   # Los serializer tienen los metodos CREATE - VALIDATE
   # def validate -> Validaciones de la data
   # def create  -> Lo que se va insertar en la b

   # pero aqui entra la data ya validada
   # validated_data = {
   # usuername: arnold
   # password: 123456
   # emial : a@a.com
   # first_name: arnold
   # last_name: gallegos
   # }
   def create(self, validated_data):
      user = User.objects.create(
         username = validated_data['username'],
         email = validated_data['email'],
         first_name = validated_data['first_name'],
         last_name = validated_data['last_name']
      )
      # Ya nos encontramos encriptando la contraseña
      user.set_password(validated_data['password'])
      user.save()
      return user