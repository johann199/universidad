from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrar),
    path('editarCurso/<codigo>', views.editar),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminar)
]
