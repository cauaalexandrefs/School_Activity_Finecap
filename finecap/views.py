from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservas
from .forms import ReservaForm


# Create your views here.

def index(request):
    reservas = Reservas.objects.all()
    total_reservas = Reservas.objects.count()
    context = {
        'reservas': reservas,
        'total_reservas': total_reservas, 
    }
    return render(request, 'finecap/index.html', context)


def detail(request, id):
    reserva = get_object_or_404(Reservas, pk=id)
    context = {
        'reserva': reserva
    }
    return render(request, 'finecap/detalhar.html', context)


def remove_reserva(request, id):
    reserva = get_object_or_404(Reservas, pk=id)
    reserva.delete()
    return redirect('index')


def create_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaForm()
            return redirect('index')
    else:
        form = ReservaForm()
    return render(request, 'finecap/forms.html', {'form': form})