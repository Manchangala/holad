# gestion/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Cliente, Pedido, DetallePedido, Domiciliario, Entrega
from django.utils import timezone
from django.contrib.auth.decorators import login_required



def lista_domiciliarios(request):
    domiciliarios = Domiciliario.objects.all()
    return render(request, 'gestion/lista_domiciliarios.html', {'domiciliarios': domiciliarios})

def crear_domiciliario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        medio_transporte = request.POST['medio_transporte']
        licencia_conduccion = request.POST['licencia_conduccion']
        fecha_vencimiento_licencia = request.POST['fecha_vencimiento_licencia']
        disponibilidad_inicio = request.POST['disponibilidad_inicio']
        disponibilidad_fin = request.POST['disponibilidad_fin']
        Domiciliario.objects.create(
            nombre=nombre, 
            apellido=apellido, 
            medio_transporte=medio_transporte, 
            licencia_conduccion=licencia_conduccion,
            fecha_vencimiento_licencia=fecha_vencimiento_licencia,
            disponibilidad_inicio=disponibilidad_inicio,
            disponibilidad_fin=disponibilidad_fin
        )
        return redirect('lista_domiciliarios')
    return render(request, 'gestion/crear_domiciliario.html')

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'gestion/lista_pedidos.html', {'pedidos': pedidos})


def crear_pedido(request):
    if request.method == 'POST':
        cliente_id = request.POST['cliente_id']
        direccion_entrega = request.POST['direccion_entrega']
        recogida_en_tienda = request.POST.get('recogida_en_tienda', False) == 'on'
        cliente = Cliente.objects.get(id=cliente_id)
        pedido = Pedido.objects.create(
            cliente=cliente,
            direccion_entrega=direccion_entrega,
            recogida_en_tienda=recogida_en_tienda
        )

        # Asignar domiciliario
        domiciliario = Domiciliario.objects.filter(fecha_vencimiento_licencia__gt=timezone.now()).first()
        if domiciliario:
            pedido.domiciliario = domiciliario
            pedido.fecha_envio = timezone.now()
            pedido.save()
        
        return redirect('lista_pedidos')
    
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'gestion/crear_pedido.html', {'clientes': clientes, 'productos': productos})

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
