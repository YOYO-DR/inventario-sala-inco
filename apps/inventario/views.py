from django.shortcuts import render
from django.views.generic import TemplateView

class InicioView(TemplateView):
    template_name='inventario/inicio.html'
