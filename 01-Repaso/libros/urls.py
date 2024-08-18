# Esto del path es de ley
from django.urls import path
from .views import GeneroListCreate, GeneroPutDelete

urlpatterns = [
   #                 Los views deben de ir acompañados
   #                 de un    .as_view()
   path('generos/', GeneroListCreate.as_view()),
   path('generos/<int:pk>/', GeneroPutDelete.as_view())
]