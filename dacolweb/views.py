from django.shortcuts import render, get_object_or_404

#DACol
import requests
import pandas as pd

def dataset_detail(request, uuid):
    ## dataset
    data = pd.read_json('https://www.datos.gov.co/resource/'+uuid+'.json')
    metadata = requests.get('https://www.datos.gov.co/api/views/metadata/v1/'+uuid).json()

    context = {
        'metadata': metadata,
        'data': data,
    }

    return render(request, 'portal/dataset_detail.html', context)

def dataset_general(request):

    ## API general
    ## -una consulta inicial para conocer la cantidad
    obtener_cantidad = requests.get('http://api.us.socrata.com/api/catalog/v1?domains=www.datos.gov.co&offset=0&limit=1').json()
    cantidad = obtener_cantidad['resultSetSize']


    ## - traerlos todos para procesar y evaluar (métricas)


    ##Para mostrar se traen los 100 más recientes
    ####mostrar = requests.get('http://api.us.socrata.com/api/catalog/v1?domains=www.datos.gov.co&order=createdAt&offset=0&limit=10000').json() #intentando pintar 10000 maté mi servidor ¡ojo!
    mostrar = requests.get('http://api.us.socrata.com/api/catalog/v1?domains=www.datos.gov.co&order=createdAt').json()

    context = {
        'mostrar': mostrar,
    }

    return render(request, 'portal/dataset_general.html', context)

def home(request):

    context = {
        'otro': "Hola mundo",
    }

    return render(request, 'portal/dataset_intro.html', context)
