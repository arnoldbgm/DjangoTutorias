# Para hacer la modificacion de la tabla de usuarios de Django
# Debo de importar lo siguiente

# Esto me jala toda la tabla de usuarios de Django
from django.contrib.auth.models import AbstractUser
from django.db import models

# Cuando hallas terminado de configuar tu usuario personalizado en Django, debe de ir
# al archivo settings.py para configurar el modelo
class CustomUser(AbstractUser):
   imagen = models.ImageField(upload_to='profile_images/', null=True, blank=True)
   dni = models.CharField(max_length=255, null=False, blank=False)
   telefono = models.CharField(max_length=15, null=True, blank=True)
