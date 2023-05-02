from django.shortcuts import render
import pandas as pd
import csv

# Create your views here.
def home(request): 
    return render (request, 'Home/home.html')

def mostrar_listado(request):
    archivo_csv = 'Home/listados/Home/LISTAWEB25.csv'
    datos = []
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return render(request, 'Home/listado.html', {'datos': datos})