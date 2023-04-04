from django.shortcuts import render, redirect
from Pago.forms import *
from Pago.models import *

# Create your views here.
def MetodosDePago(request):
    return render (request, 'Pago/metodosdepago.html')

def aplicar_cupon(request):
    if request.method == 'POST':
        form = CuponForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            if codigo == 'CRP30OFF'
                try:
                    cupon = Cupon.objects.get(codigo=codigo)
                except Cupon.DoesNotExist:
                    return render(request, 'Pago/cupon_invalido.html')
                return redirect('pagar-descuento-valido-30')
            else:
                try:
                    cupon = Cupon.objects.get(codigo=codigo)
                except Cupon.DoesNotExist:
                    return render(request, 'Pago/cupon_invalido.html')
                return redirect('pagar-descuento-valido')
    else:
        form = CuponForm()
    return render(request, 'Pago/cupondescuento.html', {'form': form})

def mostrar_descuento(request):
    return render(request, 'Pago/cupon_valido.html')

def mostrar_super_descuento(request):
    return render(request, 'Pago/cupon30_valido.html')