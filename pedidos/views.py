from django.shortcuts import render
from .models import Categoria, Produto

def inicio(request):
    categorias = Categoria.objects.prefetch_related('produtos').all()
    return render(request, 'pedidos/inicio.html', {
        'categorias': categorias,
    })