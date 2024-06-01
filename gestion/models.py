# gestion/models.py
from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    



class Domiciliario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    medio = models.CharField(max_length=50)  # Carro, moto, bicicleta, etc.
    licencia_conduccion = models.CharField(max_length=100, blank=True, null=True)
    fecha_vencimiento_licencia = models.DateField(blank=True, null=True)
    horario_disponibilidad = models.CharField(max_length=50)  # Define el formato que prefieras

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.medio}'



class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    direccion_entrega = models.CharField(max_length=255, default='Sin dirección')
    recogida_en_tienda = models.BooleanField(default=False)
    domiciliario = models.ForeignKey(Domiciliario, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_envio = models.DateTimeField(null=True, blank=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Pedido {self.id} de {self.cliente.nombre}'



class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"





class Entrega(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    domiciliario = models.ForeignKey(Domiciliario, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    direccion_entrega = models.CharField(max_length=255)

    def __str__(self):
        return f"Entrega {self.id} por {self.domiciliario.nombre}"

