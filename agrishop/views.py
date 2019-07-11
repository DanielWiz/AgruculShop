from django.shortcuts import render, redirect
from .models import Producto
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import UserCreationForm
from django.template import loader

# Create your views here.
def inicio(request):
    return render(request, 'agrishop/index.html', {})

def login(request):
	return render(request, 'agrishop/login.html', {})

def cargarRegistro(request):
	return render(request, 'registration/registro.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def cargarFormularioProducto(request):
    return render(request, 'agrishop/formularioProducto.html', {})

def guardarProducto(request):
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    imagen_producto = request.FILES['txtImagenProducto']
    stock = request.POST['txtStock']  
    p = Producto(nombre =nombre ,descripcion = descripcion ,precio = precio ,imagen_producto = imagen_producto ,stock = stock)
    p.save()
    return render(request, 'agrishop/guardarProducto.html', {'nombre': nombre})

def listadoProductos(request):
    cargarProductos = Producto.objects.all()
    template = loader.get_template('agrishop/listadoProductos.html')
    context = {
        'productos' : cargarProductos,
    }
    return HttpResponse(template.render(context, request))