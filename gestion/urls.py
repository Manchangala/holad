# gestion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('producto/<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('cliente/crear/', views.crear_cliente, name='crear_cliente'),
    path('domiciliarios/', views.lista_domiciliarios, name='lista_domiciliarios'),
    path('domiciliario/crear/', views.crear_domiciliario, name='crear_domiciliario'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedido/crear/', views.crear_pedido, name='crear_pedido'),
]
