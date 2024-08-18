from django.db import models

class GeneroModel(models.Model):
   nombre = models.CharField(max_length=255)
   class Meta:
      db_table = 'generos'

class LibrosModel(models.Model):
   titulo = models.CharField(max_length=150)
   autor = models.CharField(max_length=100)
   fecha_publicacion = models.DateField()
   genero = models.ForeignKey(GeneroModel, on_delete=models.PROTECT)

   class Meta:
      db_table = 'libros'

   #models.PROTECT
   #models.CASCADE

# Una vez terminado los modelos debemos de ejecutar un
# python manage.py makemigrations