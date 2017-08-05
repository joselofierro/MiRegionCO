from django.shortcuts import render

from apps.estadistica.models import *


def IngresosVSVisualizaciones(opcion_escogida):
    cantidad_ingresos = Ingreso.objects.all().count()
    cantidad_visualizaciones = VisualizarNoticia.objects.all().count()

    labels = ['Ingresos', 'Visualizaciones']

    return {'labels': labels, 'datos': [cantidad_ingresos, cantidad_visualizaciones], 'titulo': opcion_escogida}


def IngresosVSCompartir(opcion_escogida):
    cantidad_ingresos = Ingreso.objects.all().count()
    cantidad_compartida = CompartirNoticia.objects.all().count()

    labels = ['Ingresos', 'Comparten']

    return {'labels': labels, 'datos': [cantidad_ingresos, cantidad_compartida], 'titulo': opcion_escogida}


def IngresosVSGuardan(opcion_escogida):
    cantidad_ingresos = Ingreso.objects.all().count()
    cantidad_guardan = GuardarNoticia.objects.all().count()

    labels = ['Ingresos', 'Guardan']

    return {'labels': labels, 'datos': [cantidad_ingresos, cantidad_guardan], 'titulo': opcion_escogida}


def IngresosVsVisitan(opcion_escogida):
    cantidad_ingresos = Ingreso.objects.all().count()
    cantidad_visitan = VisitarSitio.objects.all().count()

    labels = ['Ingresos', 'Visitan']

    return {'labels': labels, 'datos': [cantidad_ingresos, cantidad_visitan], 'titulo': opcion_escogida}


def IngresosVsLlaman(opcion_escogida):
    cantidad_ingresos = Ingreso.objects.all().count()
    cantidad_llaman = LlamarSitio.objects.all().count()

    labels = ['Ingresos', 'Llaman']

    return {'labels': labels, 'datos': [cantidad_ingresos, cantidad_llaman], 'titulo': opcion_escogida}


def Ingresos(opcion_escogida):
    cantidad_ingresos = Ingreso.objects.all().count()

    labels = ['Ingresos']

    return {'labels': labels, 'datos': [cantidad_ingresos], 'titulo': opcion_escogida}


def IngresosVSFacebook(opcion_escogida):
    cantidad_ingresos = Ingreso.objects.all().count()
    cantidad_facebook = FacebookSitio.objects.all().count()
    labels = ['Ingresos', 'Facebook']

    return {'labels': labels, 'datos': [cantidad_ingresos, cantidad_facebook], 'titulo': opcion_escogida}


def IngresosVSInstagram(opcion_escogida):
    cantidad_ingresos = Ingreso.objects.all().count()
    cantidad_instagram = InstagramSitio.objects.all().count()

    labels = ['Ingresos', 'Instagram']

    return {'labels': labels, 'datos': [cantidad_ingresos, cantidad_instagram], 'titulo': opcion_escogida}


def Estadisticas(request):
    lista_opciones = ['Ingreso Vs Visualizaciones', 'Ingresos Vs Comparten', 'Ingresos Vs Guardan',
                      'Ingresos Vs Visitan', 'Ingresos Vs Llaman', 'Ingresos Vs Facebook', 'Ingresos Vs Instagram',
                      'Ingresos']

    if request.method == 'GET':
        return render(request, 'estadistica/chart.html', {'opciones': lista_opciones}, content_type='text/html')

    elif request.method == 'POST':
        # opciones de la lista
        opcion_escogida = request.POST.getlist('opciones')[0]
        # posicion de la opcion en la lista
        index = lista_opciones.index(opcion_escogida)
        # diccionario a almacenar
        diccionario = {}

        if index == 0:
            diccionario = IngresosVSVisualizaciones(opcion_escogida)
        elif index == 1:
            diccionario = IngresosVSCompartir(opcion_escogida)
        elif index == 2:
            diccionario = IngresosVSGuardan(opcion_escogida)
        elif index == 3:
            diccionario = IngresosVsVisitan(opcion_escogida)
        elif index == 4:
            diccionario = IngresosVsLlaman(opcion_escogida)
        elif index == 5:
            diccionario = IngresosVSFacebook(opcion_escogida)
        elif index == 6:
            diccionario = IngresosVSInstagram(opcion_escogida)
        elif index == 7:
            diccionario = Ingresos(opcion_escogida)

        return render(request, 'estadistica/chart.html', diccionario, content_type='text/html')
