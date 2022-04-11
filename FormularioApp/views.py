from django.shortcuts import render
from django.http import HttpResponse
from .reportes import ReportePersona

def reporte_personas(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="personas.pdf"'
    r = ReportePersona()
    response.write(r.run())
    return response


