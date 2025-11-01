from django.shortcuts import render
from .models import Receta

# Create your views here.
def lista_recetas(request):
    recetas=Receta.objects.all()
    context={'recetas':recetas}
    for receta in recetas:
        receta.ingredientes_lista = [i.strip() for i in receta.ingredientes.split('•')]
    return render (request, 'receta_list.html', context)