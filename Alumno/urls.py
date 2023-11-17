from .views import * 
from django.urls import path

urlpatterns = [
    path('', Inicio ,name='inicio'),
    path('agregar/', Agregar, name="agregar"),
    path('editar/<int:id>', Editar, name="editar"),
    path('borrar/<int:id>', Borrar, name="borrar"),
    path('detalles/<int:id>', Detalles, name="detalle"),
]