from django.shortcuts import render, redirect
from .models import Producto, User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import UserCreationForm
from django.template import loader
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.
def inicio(request):
    cargarProductos = Producto.objects.all()
    template = loader.get_template('agrishop/index.html')
    context = {
        'productos' : cargarProductos,
    }
    return HttpResponse(template.render(context, request))

def mapa(request):
    return render(request, 'agrishop/mapa.html', {})

def login(request):
	return render(request, 'agrishop/login.html', {})

def cargarRegistro(request):
	return render(request, 'registration/registro.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.Fecha_Nacimiento = form.cleaned_data.get('Fecha_Nacimiento')
            user.profile.Rut = form.cleaned_data.get('Rut')
            user.profile.Nombre = form.cleaned_data.get('Nombre')
            user.profile.Apellido = form.cleaned_data.get('Apellido')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/registro.html', {'form': form})

def cargarFormularioProducto(request):
    return render(request, 'agrishop/formularioProducto.html', {})

def guardarProducto(request):
    user = request.user
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    imagen_producto = request.FILES['txtImagenProducto']
    stock = request.POST['txtStock']  
    p = Producto(Usuario=user,nombre=nombre ,descripcion = descripcion ,precio = precio ,imagen_producto = imagen_producto ,stock = stock)
    p.save()
    return render(request, 'agrishop/guardarProducto.html', {'nombre': nombre})

def listadoProductos(request):
    cargarProductos = Producto.objects.all()
    template = loader.get_template('agrishop/listadoProductos.html')
    context = {
        'productos' : cargarProductos,
    }
    return HttpResponse(template.render(context, request))

def administrarProductos(request, usuario_id): 
    user = request.user
    cargarProductos = Producto.objects.filter(Usuario = user)    
    template = loader.get_template('agrishop/administrarProductos.html')
    context = {
        'productos' : cargarProductos,
    }
    return HttpResponse(template.render(context, request))

def borrarProducto(request, producto_id):
    productoParaBorrar = Producto.objects.get(pk=producto_id)
    productoParaBorrar.delete()
    return render(request, 'agrishop/productoEliminado.html')

def detalleProducto(request, producto_id):
    productoEncontrado = Producto.objects.get(pk=producto_id)
    return render(request, 'agrishop/detalleProducto.html', {'productoEncontrado':productoEncontrado})

def modificarProducto(request, producto_id):
    productoAActualizar=Producto.objects.get(pk=producto_id)
    return render(request, 'agrishop/formularioActualizarProducto.html', {'productoAActualizar':productoAActualizar})

def confirmarModificacion(request, producto_id):
    productoModificado = Producto.objects.get(pk=producto_id)
    productoModificado.nombre=request.POST["txtNuevoNombre"]
    productoModificado.descripcion=request.POST["txtNuevoDescripcion"]
    productoModificado.precio=request.POST["txtNuevoPrecio"]
    productoModificado.stock=request.POST["txtNuevoStock"]  
    productoModificado.imagen_producto=request.FILES["txtNuevoImagen"]     
    productoModificado.save()
    return render(request, 'agrishop/confirmarModificacion.html' , {'productoModificado.nombre':productoModificado.nombre})