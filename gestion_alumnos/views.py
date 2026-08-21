from django.shortcuts import render

from .models import Alumno


def inicio(request):
    alumnos = Alumno.objects.all()

    contexto = {
        "alumnos": alumnos
    }

    return render(
        request,
        "gestion_alumnos/inicio.html",
        contexto
    )