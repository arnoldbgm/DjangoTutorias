# Toda la logica de mi endpoint se encuentra en el VIEW
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GeneroModel
from .serializers import GeneroSerializer

# El nombre de la clase no importa
# Lo importante es la herencia  ' ( APIView ) '
class GeneroListCreate(APIView):
   def get(self, request):
      # SELECT * FROM generos;
      # Para usar LA ORM
      # 1. Siempre va primero el Modelo
      # 2. objects
      # 3. El metodo que quiero ejectuar
      generos = GeneroModel.objects.all()
      serializer = GeneroSerializer(generos, many=True)
      return Response(serializer.data)

   def post(self,request):
      #
      # {
      #    "nombre": "Novela"
      # }
      #
      serializer = GeneroSerializer(data=request.data)
      if serializer.is_valid():
         # GeneroModel.objects.create(nombre="Novela", descripcion="asda", ...)
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)
   
class GeneroPutDelete(APIView):
   pass