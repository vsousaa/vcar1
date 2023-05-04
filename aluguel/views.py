from django.shortcuts import render, redirect
from .models import Car, Aluguel
from .forms import AluguelForm,ClienteForm,CarForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_carros(request):
    carros = Car.objects.all()
    return render(request, "car/lista.html",{"carros":carros})

def detalhar_car(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request, 'car/detalhes.html', {"car":car})

def realizar_aluguel(request):
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm()
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm()
        return render(request, "aluguel/cadastrar.html", {'form': form})

def realizar_aluguel_car(request, car_pk):
    print(car_pk)
    car = Car.objects.get(id=car_pk)
    aluguel = Aluguel()
    aluguel.carro  = car
    
    form = AluguelForm(instance=aluguel)
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm(instance=aluguel)
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm(instance=aluguel)
        return render(request, "aluguel/cadastrar.html", {'form': form})
    
def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = ClienteForm()
            return render(request, "cliente/cadastrar.html", {'form': form})
    else:
        form = ClienteForm()
        return render(request, "cliente/cadastrar.html", {'form': form})
    

def cadastrar_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = CarForm()
            return render(request, "car/cadastrar.html", {'form': form})
    else:
        form = CarForm()
        return render(request, "car/cadastrar.html", {'form': form})