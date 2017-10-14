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


def IngresoLoginE(opcion_escogida):
    cantidad_ingresos = IngresoLogin.objects.all().count()
    labels = ['IngresoLogin']

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


def Visitindex(opcion_escogida):
    cantidad_visit = VisitIndex.objects.all().count()

    labels = ['Visita index']

    return {'labels': labels, 'datos': [cantidad_visit], 'titulo': opcion_escogida}


def Visitnews(opcion_escogida):
    cantidad_visit = VisitNews.objects.all().count()

    labels = ['Visita noticias']

    return {'labels': labels, 'datos': [cantidad_visit], 'titulo': opcion_escogida}


def Sharefacebook(opcion_escogida):
    cantidad_share = ShareFacebook.objects.all().count()

    labels = ['Compartir Facebook']

    return {'labels': labels, 'datos': [cantidad_share], 'titulo': opcion_escogida}


def Sharetwitter(opcion_escogida):
    cantidad_share = ShareTwitter.objects.all().count()

    labels = ['Compartir Twitter']

    return {'labels': labels, 'datos': [cantidad_share], 'titulo': opcion_escogida}


def Sharegoogle(opcion_escogida):
    cantidad_share = ShareGoogle.objects.all().count()

    labels = ['Compartir Google']

    return {'labels': labels, 'datos': [cantidad_share], 'titulo': opcion_escogida}


def Visitmap(opcion_escogida):
    cantidad_share = VisitMap.objects.all().count()

    labels = ['Visitar Mapa']

    return {'labels': labels, 'datos': [cantidad_share], 'titulo': opcion_escogida}


def Visitplace(opcion_escogida):
    cantidad_share = VisitPlace.objects.all().count()

    labels = ['Visitar sitio']

    return {'labels': labels, 'datos': [cantidad_share], 'titulo': opcion_escogida}


def Savenews(opcion_escogida):
    cantidad_share = SaveNews.objects.all().count()

    labels = ['Guardar Noticia']

    return {'labels': labels, 'datos': [cantidad_share], 'titulo': opcion_escogida}


# metodo principal con todas la estadisticas
def Estadisticas(request):
    lista_opciones = ['Ingreso Vs Visualizaciones', 'Ingresos Vs Comparten', 'Ingresos Vs Guardan',
                      'Ingresos Vs Visitan', 'Ingresos Vs Llaman', 'Ingresos Vs Facebook', 'Ingresos Vs Instagram',
                      'Ingresos', 'IngresoLogin', 'Visitar index', 'Visitar noticias', 'Compartir facebook',
                      'Compartir twitter', 'Compartir google', 'Visitar mapa', 'Visitar lugar', 'Guarda noticias']

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
        elif index == 8:
            diccionario = IngresoLoginE(opcion_escogida)
        elif index == 9:
            diccionario = Visitindex(opcion_escogida)
        elif index == 10:
            diccionario = Visitnews(opcion_escogida)
        elif index == 11:
            diccionario = Sharefacebook(opcion_escogida)
        elif index == 12:
            diccionario = Sharetwitter(opcion_escogida)
        elif index == 13:
            diccionario = Sharegoogle(opcion_escogida)
        elif index == 14:
            diccionario = Visitmap(opcion_escogida)
        elif index == 15:
            diccionario = Visitplace(opcion_escogida)
        elif index == 16:
            diccionario = Savenews(opcion_escogida)

        return render(request, 'estadistica/chart.html', diccionario, content_type='text/html')
