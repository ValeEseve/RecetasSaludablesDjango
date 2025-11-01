from django.shortcuts import render
from .models import Receta
from django.shortcuts import get_object_or_404


# Create your views here.
def lista_recetas(request):
    recetas=Receta.objects.all()
    context={'recetas':recetas}
    for receta in recetas:
        receta.ingredientes_lista = [i.strip() for i in receta.ingredientes.split('•')]
    return render (request, 'receta_list.html', context)

def detalle_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    ingredientes_lista = [i.strip() for i in receta.ingredientes.split('•')]
    receta.ingredientes_lista = ingredientes_lista
    return render(request, 'detalle_receta.html', {'receta': receta})