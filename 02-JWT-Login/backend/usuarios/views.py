# Ahora crearemos el enpoint para registrar mis usuarios

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework import generics

class UserRegister(APIView):
# debes de especificar de que metodo es POST - GET - PUT - PATCH - DELETE
   def post(self, request):
   #  {
   # usuername: arnold
   # password: 123456
   # emial : a@a.com
   # first_name: arnold
   # last_name: gallegos
   # }
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({
            "msg": "Registro exitoso 😁😁",
            "content": serializer.data
         }, status = status.HTTP_201_CREATED)
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
   


class UserRegister(generics.CreateAPIView):
   serializer = UserSerializer(data=request.data)

   def create(self, request):
      if self.serializer.is_valid():
         self.serializer.save()
         return Response({
            "msg": "Registro exitoso 😁😁",
            "content": self.serializer.data
         }, status = status.HTTP_201_CREATED)
      return Response(self.serializer.errors, status = status.HTTP_400_BAD_REQUEST)

