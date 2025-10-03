from django.urls import path
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarea
from .forms import TareaForm

app_name = 'tareas'

class TareaLista(ListView):
    model = Tarea
    paginate_by = 10
    context_object_name = 'tareas'

    def get_queryset(self):
        qs = Tarea.objects.all()
        vigente = self.request.GET.get('vigente')
        prioridad = self.request.GET.get('prioridad')
        
        if vigente in ('true', 'false'):
            qs = qs.filter(vigente=(vigente == 'true'))
        if prioridad:
            qs = qs.filter(prioridad=prioridad)
            
        return qs.order_by('-fecha_creacion')

class TareaDetalle(DetailView):
    model = Tarea

class TareaCrear(CreateView):
    model = Tarea
    form_class = TareaForm
    success_url = reverse_lazy('tareas:tarea_list')

class TareaEditar(UpdateView):
    model = Tarea
    form_class = TareaForm
    success_url = reverse_lazy('tareas:tarea_list')

class TareaEliminar(DeleteView):
    model = Tarea
    success_url = reverse_lazy('tareas:tarea_list')

urlpatterns = [
    path('', TareaLista.as_view(), name='tarea_list'),
    path('<int:pk>/', TareaDetalle.as_view(), name='tarea_detail'),
    path('nueva/', TareaCrear.as_view(), name='tarea_create'),
    path('<int:pk>/editar/', TareaEditar.as_view(), name='tarea_update'),
    path('<int:pk>/eliminar/', TareaEliminar.as_view(), name='tarea_delete'),
]