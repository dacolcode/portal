from django.shortcuts import render, get_object_or_404

#DACol
import requests
import pandas as pd

#gráficas
import matplotlib as pl
import matplotlib.pyplot as plt

def home(request):

    context = {
        'mensaje': "Aquí poner una intro bien guapa",
    }

    #return render(request, 'portal/dataset_intro.html', context)
    return render(request, 'portal/index.html', context)

def tablas(request):
    return render(request, 'portal/tables.html')

def graficas(request):

    ## por categorias
    facets = requests.get('http://api.us.socrata.com/api/catalog/v1/domains/www.datos.gov.co/facets').json()
    respuesta = facets[0]['values']

    categorias = []
    valores = []
    for categoria in respuesta:
        categorias.append(categoria['value'])
        valores.append(categoria['count'])

    data = {
        'categorias': respuesta,
    }
    return render(request, 'portal/charts.html',data)

def dataset_detail(request, uuid):
    ## dataset
    data = pd.read_json('https://www.datos.gov.co/resource/'+uuid+'.json')
    metadata = requests.get('https://www.datos.gov.co/api/views/metadata/v1/'+uuid).json()
    metadataPlus = requests.get('http://api.us.socrata.com/api/catalog/v1?ids='+uuid).json()

    #derivados
    derivados = requests.get('http://api.us.socrata.com/api/catalog/v1?derived_from'+uuid).json()

    #otras mismo dueño
    id_autor =  metadataPlus['results'][0]['owner']['id']
    otros_autor = requests.get('http://api.us.socrata.com/api/catalog/v1?derived_from'+ id_autor).json()


    context = {
        'metadata': metadata,
        'data': data,
        'metadataPlus': metadataPlus['results'][0]['owner']['id'],
    }

    return render(request, 'portal/dataset_detail.html', context)

def dataset_general(request):

    ## API general
    ## -una consulta inicial para conocer la cantidad
    obtener_cantidad = requests.get('http://api.us.socrata.com/api/catalog/v1?domains=www.datos.gov.co&offset=0&limit=1').json()
    cantidad = obtener_cantidad['resultSetSize']

    ## por categorias
    facets = requests.get('http://api.us.socrata.com/api/catalog/v1/domains/www.datos.gov.co/facets').json()
    categorias = facets[0]


    ## - traerlos todos para procesar y evaluar (métricas)


    ##Para mostrar se traen los 100 más recientes
    ####mostrar = requests.get('http://api.us.socrata.com/api/catalog/v1?domains=www.datos.gov.co&order=createdAt&offset=0&limit=10000').json() #intentando pintar 10000 maté mi servidor ¡ojo!
    mostrar = requests.get('http://api.us.socrata.com/api/catalog/v1?domains=www.datos.gov.co&order=createdAt&only=datasets').json()

    context = {
        'mostrar': mostrar,
        'categorias': categorias,
    }

    return render(request, 'portal/dataset_general.html', context)

from django.http import JsonResponse
def consultar_categorias(request):

    ## por categorias
    facets = requests.get('http://api.us.socrata.com/api/catalog/v1/domains/www.datos.gov.co/facets').json()
    respuesta = facets[0]['values']

    categorias = []
    valores = []
    for categoria in respuesta:
        categorias.append(categoria['value'])
        valores.append(categoria['count'])

    data = {
        'categorias': categorias,
        'valores': valores,
    }

    return JsonResponse(data)