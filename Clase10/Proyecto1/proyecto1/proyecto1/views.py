from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime

def probando_templates(request):
    # Lista de notas del 1 al 10
    lista_de_notas = [1, 2, 5, 8, 7, 9, 10, 3, 2]

    # Contexto que incluye la lista de notas
    contexto = {
        'variable': 'Hola desde la vista probando_templates!',
        'notas': lista_de_notas
    }

    # Renderiza el template con el contexto
    return render(request, 'index.html', contexto)
