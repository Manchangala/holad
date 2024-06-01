# gestion/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Cliente, Pedido, DetallePedido, Domiciliario, Entrega
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm, DomiciliarioForm, ClienteForm, PedidoForm





def lista_domiciliarios(request):
    domiciliarios = Domiciliario.objects.all()
    return render(request, 'gestion/lista_domiciliarios.html', {'domiciliarios': domiciliarios})

def crear_domiciliario(request):
    if request.method == 'POST':
        form = DomiciliarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_domiciliarios')
    else:
        form = DomiciliarioForm()
    return render(request, 'gestion/crear_domiciliario.html', {'form': form})
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'gestion/lista_pedidos.html', {'pedidos': pedidos})


def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            # Asignar domiciliario
            domiciliario = Domiciliario.objects.filter(fecha_vencimiento_licencia__gt=timezone.now()).first()
            if domiciliario:
                pedido.domiciliario = domiciliario
                pedido.fecha_envio = timezone.now()
                pedido.save()
                return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'gestion/crear_pedido.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion/lista_clientes.html', {'clientes': clientes})


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'gestion/crear_cliente.html', {'form': form})

# Vistas para Producto
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestion/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'gestion/detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'gestion/crear_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.categoria = request.POST['categoria']
        producto.save()
        return redirect('detalle_producto', producto_id=producto.id)
    return render(request, 'gestion/editar_producto.html', {'producto': producto})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'gestion/eliminar_producto.html', {'producto': producto})
