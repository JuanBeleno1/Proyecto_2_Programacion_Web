from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .models import Tenis

# Create your views here.
def index(request):

    lista_tenis = Tenis.objects.all()
    template = loader.get_template("index.html")
    context = {"tenis":lista_tenis}
    return HttpResponse(template.render(context,request))


def vista_detalle(request, id_tenis):

    detalle_tenis = Tenis.objects.get(id = id_tenis)

    template = loader.get_template("detail.html")

    context = {"tenis":detalle_tenis}

    return HttpResponse(template.render(context,request))