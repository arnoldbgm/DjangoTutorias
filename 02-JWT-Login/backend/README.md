# Django JWT Authentication 🦾🐍

Este proyecto muestra cómo implementar un sistema de autenticación en Django utilizando JWT para proteger las rutas. Implementaremos un registro y un login para los usuarios.

## Requisitos Previos

- **Django**: Debes tener instalado Django en tu entorno.
- **Django REST Framework (DRF)**: Necesitamos DRF para crear nuestras API views.
- **Django REST Framework SimpleJWT**: Para manejar la autenticación con JWT.

## Instalación

Primero, instala Django, Django REST Framework y SimpleJWT:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

## Configuración

Agrega las siguientes aplicaciones a tu archivo `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework_simplejwt',  # Añadir esta línea
]

# Configuración de DRF para JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=100),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=100),
}

```

## Serializadores

Creamos un `UserSerializer` para manejar la creación de usuarios:

```python
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
```

## Vistas

Implementamos la vista para el registro de usuarios:

```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "msg": "Registro exitoso",
                "content": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

## URLs

Finalmente, configuramos las rutas para las vistas:

```python
from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view())
]
```

## Prueba del Registro

Para probar el registro, puedes utilizar herramientas como Postman o cURL. Envía una petición `POST` a la ruta `/register/` con un cuerpo JSON que contenga el `username`, `password`, `email`, `first_name` y `last_name`.

---
