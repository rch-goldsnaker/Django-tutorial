#Importamos el modulo HttpResponse

from django.http import HttpResponse
#Importamos el modulo time

import datetime

#Para crear una vista lo hacemos mediante una funcion :
#Tener en cuenta tiene que recibir un request como argumento.
#es como una funcion vista.

def saludo(request):
    return HttpResponse("Hola esta la primer pagina con rango")

#ahora debemos enlazar esta vista con un URLS, de aca vamos al
# archivo urls.py 

def despedida(request):
    return HttpResponse("Adios")

# definimos una nueva funcion fecha.
def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="la fecha actual es %s" %fecha_actual
    return HttpResponse(documento)

# vamos a crear una vista que calcula tu edad,
# vamos a enviarle un parametro, para pasarle por url

def calculaEdad(request, edad,agno):

    periodo=agno-2021
    edadFutura=edad+periodo
    documento="en el año %s tendras %s años" %(agno,edadFutura)
    return HttpResponse(documento)

