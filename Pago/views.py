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
            try:
                cupon = Cupon.objects.get(codigo=codigo)
                if cupon.porcentaje_descuento == 30:
                    return redirect('pagar-descuento-valido-30')
                else:
                    return redirect('pagar-descuento-valido')
            except Cupon.DoesNotExist:
                return render(request, 'Pago/cupon_invalido.html')
    else:
        form = CuponForm()
    return render(request, 'Pago/cupondescuento.html', {'form': form})

def mostrar_descuento(request):
    return render(request, 'Pago/cupon_valido.html')

def mostrar_super_descuento(request):
    return render(request, 'Pago/cupon30_valido.html')