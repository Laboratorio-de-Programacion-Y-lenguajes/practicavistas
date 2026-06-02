from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Curso
from .forms import CursoForm

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.contrib.auth import views as auth_views


class CursoListView(ListView):
    model = Curso
    template_name = "academia/lista_cursos.html"
    context_object_name = "cursos"  # Nombre para usar en el template

    def get_queryset(self):
        return Curso.objects.all().order_by("fecha_inicio")


class CursoDetailView(DetailView):
    model = Curso
    template_name = "academia/detalle_curso.html"
    context_object_name = "curso"


class CursoCreateView(
    LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, CreateView
):
    model = Curso
    form_class = CursoForm
    template_name = "academia/curso_form.html"
    success_url = reverse_lazy("lista_cursos")
    success_message = "El curso fue creado exitosamente."
    login_url = "/login/"

    def test_func(self):
        # Verificamos si el usuario tiene un perfil de instructor
        return hasattr(self.request.user, "perfil_instructor")


class CursoUpdateView(UpdateView):
    model = Curso
    fields = ["titulo", "fecha_inicio"]
    template_name = "academia/curso_form.html"  # Reutilizamos el template
    success_url = reverse_lazy("lista_cursos")


class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "academia/curso_confirm_delete.html"
    success_url = reverse_lazy("lista_cursos")
