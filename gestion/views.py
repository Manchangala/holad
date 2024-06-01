# gestion/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Cliente, Pedido, DetallePedido, Domiciliario, Entrega


from .models import Cliente


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion/lista_clientes.html', {'clientes': clientes})


def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        Cliente.objects.create(nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono)
        return redirect('lista_clientes')
    return render(request, 'gestion/crear_cliente.html')


# Vistas para Producto
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestion/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'gestion/detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        categoria = request.POST['categoria']
        producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, categoria=categoria)
        producto.save()
        return redirect('lista_productos')
    return render(request, 'gestion/crear_producto.html')

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
