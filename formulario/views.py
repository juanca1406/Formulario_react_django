from django.http import JsonResponse
from .models import Registro
# Create your views here.

def formulario(request):
    productos  = Registro.objects.all()
    data = [{'nombre': producto.nombre, 'precio': producto.precio} for producto in productos]
    return JsonResponse(data, safe=False)