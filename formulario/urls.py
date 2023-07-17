from django.urls import path
from . import views

app_name='formulario'
urlpatterns = [
   path('productos/', views.formulario, name='formulario'),
]
