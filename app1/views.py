from django.db.models.fields import EmailField
from django.shortcuts import render, HttpResponse
from .models import Cliente
def inicio(request):
    #return HttpResponse("this is equivalent of @app.route!")
    return render(request,"index.html")
# Create your views here.

def agregar(request):
    #request.post['parametro']
    Cliente.objects.create(
    nombre = request.POST['nombre'],
    apellido = request.POST['apellido'],
    rut = request.POST['rut'],
    email = request.POST['email']
    )

    return render(request,"index.html")