from django.shortcuts import render
from .models import Receta

# Create your views here.
def lista_recetas(request):
    recetas=Receta.objects.all()
    context={'recetas':recetas}
    return render (request, 'receta_list.html', context)