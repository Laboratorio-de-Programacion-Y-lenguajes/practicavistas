from django.urls import path
from .views import (
    CursoListView,
    CursoDetailView,
    CursoCreateView,
    CursoUpdateView,
    CursoDeleteView,
)

urlpatterns = [
    path("cursos/", CursoListView.as_view(), name="lista_cursos"),
    path("cursos/<int:pk>/", CursoDetailView.as_view(), name="detalle_curso"),
    path("cursos/nuevo/", CursoCreateView.as_view(), name="crear_curso"),
    path("cursos/<int:pk>/editar/", CursoUpdateView.as_view(), name="editar_curso"),
    path("cursos/<int:pk>/eliminar/", CursoDeleteView.as_view(), name="eliminar_curso"),
]
