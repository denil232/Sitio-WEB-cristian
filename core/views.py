from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegistroForm, ObraForm
from .models import Obra

# --- VISTAS PÚBLICAS ---

def home(request):
    return render(request, "core/home.html")

def quienes(request):
    return render(request, 'core/quienes.html')

def preguntas(request):
    return render(request, 'core/preguntas.html')

def contacto(request):
    return render(request, 'core/contacto.html')

# Esta vista ahora es DINÁMICA: Trae las pinturas de la base de datos
def galeria(request):
    obras = Obra.objects.all() # Trae todas las obras guardadas
    context = {'obras': obras}
    return render(request, "core/galeria.html", context)


# --- VISTAS DE GESTIÓN (Solo para Cristian/Staff) ---

@staff_member_required
def agregar_obra(request):
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('galeria')
    else:
        form = ObraForm()
    return render(request, 'core/formulario_obra.html', {'form': form})

@staff_member_required
def editar_obra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('galeria')
    else:
        form = ObraForm(instance=obra)
    return render(request, 'core/formulario_obra.html', {'form': form})

@staff_member_required
def eliminar_obra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    obra.delete()
    return redirect('galeria')


# --- AUTENTICACIÓN (Login/Registro) ---

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # inicia sesión automáticamente
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'core/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect("home")
        else:
            return render(request, "core/login.html", {"error": "Usuario o contraseña incorrectos"})
    return render(request, "core/login.html")

def cerrar_sesion(request):
    logout(request)
    return redirect("home")