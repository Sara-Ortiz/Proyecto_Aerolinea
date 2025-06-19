from django.shortcuts import render, redirect
from .models import Vuelo
from .forms import VueloForm, RegistroUsuarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
#vista de inicio
def home(request):
    return render(request, 'home.html')

#Registro de usuarios 
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request,'registro.html', {'form':form})

def iniciar_sesion(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user: 
            login(request, user)
            return redirect('lista_vuelos')
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')




@login_required
def lista_vuelos(request):
    vuelo = Vuelo.objects.all()
    return render(request, 'vuelo/lista.html', {'vuelos' : vuelo})

@login_required
def agregar_vuelo(request):
    form = VueloForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_vuelos')
    return render(request, 'vuelo/form.html', {'form':form})

@login_required
def editar_vuelo(request,id):
    vuelo =  Vuelo.objects.get(id=id)
    form = VueloForm(request.POST or None, instance=vuelo)
    if form.is_valid():
        form.save()
        return redirect('lista_vuelos')
    return render( request, 'vuelo/form.html', {'form':form})



@login_required

def eliminar_vuelo(request, id):
    vuelo = Vuelo.objects.get(id=id)
    vuelo.delete()
    return redirect('lista_vuelos')