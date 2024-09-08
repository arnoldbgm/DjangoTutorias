from rest_framework import generics
from .models import ProductoModel
from .serializer import ProductoSerializer

class ProductoListCreateView(generics.ListCreateAPIView):
   queryset = ProductoModel.objects.all()
   serializer_class = ProductoSerializer