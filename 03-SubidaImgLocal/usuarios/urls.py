from django.urls import path
from .views import CreateUserView

urlpatterns = [
   path('create-user/', CreateUserView.as_view())
]