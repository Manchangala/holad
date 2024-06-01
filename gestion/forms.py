# gestion/forms.py

from django import forms
from .models import Producto, Domiciliario, Cliente, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria']

class DomiciliarioForm(forms.ModelForm):
    class Meta:
        model = Domiciliario
        fields = ['nombre', 'apellido', 'medio_transporte', 'telefono']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'direccion', 'telefono']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'productos', 'fecha_pedido', 'direccion_entrega', 'recogida_en_tienda', 'domiciliario', 'fecha_envio', 'fecha_entrega']
