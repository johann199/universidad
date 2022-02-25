from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm

# Create your views here.

def home(request):
    form = CursoForm()
    cursos = {'cursoform': form}
    return render(request, "gestionCursos.html", cursos)

def registrar(request):
    form = CursoForm()
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoForm()
    
    return render(request, 'gestionCursos.html', {'form': form})


def editar(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "editar.html", {"curso": curso})
def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos

    curso.save()

    return redirect('/')

def eliminar(request ,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')
