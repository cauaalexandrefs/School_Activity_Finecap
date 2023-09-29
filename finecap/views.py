from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservas
from .forms import ReservaForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    reservas = Reservas.objects.all().order_by('date')
    if(request.GET.get('q')):
        reservas = reservas.filter(nome_empresa__icontains=request.GET.get('q'))
    if(request.GET.get('btnradio1')):
        reservas = reservas.filter(quitado=True)
    if(request.GET.get('btnradio2')):
        reservas = reservas.filter(quitado=False)
    if(request.GET.get('valor')):
        reservas = reservas.filter(stand__valor=request.GET.get('valor'))
    if(request.GET.get('date')):
        reservas = reservas.filter(date__date=request.GET.get('date'))    
    
    paginator = Paginator(reservas, 5)
    page = request.GET.get('page')
    try:
        reservas = paginator.page(page)
    except PageNotAnInteger:
        reservas = paginator.page(1)
    except EmptyPage:
        reservas = paginator.page(paginator.num_pages)

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