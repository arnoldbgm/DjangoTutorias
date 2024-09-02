from rest_framework import generics
from .models import CustomUser
from .serializer import CustomUserSerailizer

class CreateUserView (generics.CreateAPIView):
   queryset = CustomUser.objects.all()
   serializer_class = CustomUserSerailizer