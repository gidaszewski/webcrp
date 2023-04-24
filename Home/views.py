from django.shortcuts import render
import pandas as pd

# Create your views here.
def home (request): 
    return render (request, 'Home/home.html')

def listado(request):

    df = pd.read_excel('Home/listados/Home/LISTA WEB 1.xls')

    datos = df.to_dict('records')

    return render(request, 'listado.html', {'datos': datos})
