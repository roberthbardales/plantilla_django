

from django.db.models.query import QuerySet
from django.shortcuts import render

from django.urls import reverse_lazy,reverse
from django.db.models import Q
# Create your views here.
from . import views


from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

from .forms import ProjectForm
from .managers import *
from .models import Tag,Project,Category

from .serializers import (
    Project,
    Project2Serializer,
    ProjectSerializerLink,
    PersonPagination,
    ProjectSerializer,
    CountReunionSerializer,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,  #equivalente al Detailview
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,  #update pero viendo los campos
)


class PaginaInicio(TemplateView):
    template_name = "index.html"

class ListarProyecto(ListView):
    template_name ="proyecto/list.html"
    # model = Project
    paginate_by = 4
    ordering='id'
    context_object_name = 'contexto_proyectos'
    # def get_queryset(self):
    #     return  Project.objects.all().order_by('id')

    def get_queryset(self):
        kword_id = self.request.GET.get("kword_id", '')
        kword_titulo = self.request.GET.get("kword_titulo", '')
        kword_categoria = self.request.GET.get("kword_categoria", '')
        kword_general = self.request.GET.get("kword_general", '')

        if len(kword_id)> 0:
            lista = Project.objects.filter(
                id=kword_id
                # title=palabra_obtenida
            ).order_by('-updated')
            return lista

        if len(kword_titulo)> 0:
            lista = Project.objects.buscar_proyecto_titulo(kword_titulo)
            return lista

        if len(kword_categoria)> 0:
            lista = Project.objects.buscar_proyecto_categoria(kword_categoria)
            return lista

        if len(kword_general)> 0:
            lista = Project.objects.buscar_proyecto_general(kword_general)
            return lista

        else:
            # lista_proyectos = Project.objects.all().order_by('updated')
            lista_proyectos = Project.objects.all()
            return lista_proyectos


def buscar_entrada_categoria(self,kword,categoria):
        if len(categoria)> 0:
            return self.filter(
                category__short_name=categoria,
                title__icontains=kword,

                public = True
            ).order_by('-created')


class ProyectoDetailView(DetailView):
    model = Project
    template_name = "proyecto/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        #toot un proceso
        # context['ejemplo'] = 'contexto ejemplo'
        return context


class ProyectoCreateView(CreateView):
    template_name = "proyecto/add.html"
    model = Project
    form_class = ProjectForm
    # fields=[
    #     'title',
    #     'description',
    #     'image',
    #     'tags',
    #     'category',
    # ]
    success_url=reverse_lazy('portafolio_app:listar_proyecto')


class ProyectoDeleteView(DeleteView):
    template_name = "proyecto/delete.html"
    model = Project
    success_url=reverse_lazy('portafolio_app:listar_proyecto')


class ProyectoUpdateView(UpdateView):
    template_name = "proyecto/update.html"
    model=Project
    form_class= ProjectForm
    success_url=reverse_lazy('portafolio_app:listar_proyecto')

    def form_valid(self, form):

        return super(ProyectoUpdateView, self).form_valid(form)

class ListarProyectoByKword(ListView):
    template_name ="proyecto/list.html"
    context_object_name = 'contexto_by_kword'

class ProyectosPorEtiquetaListView(ListView):
    model = Project
    template_name = 'proyecto/pruebas.html'
    context_object_name = 'proyectos_por_etiquetas'

    def get_queryset(self):
        etiqueta_id = self.kwargs['etiqueta_id']
        etiqueta = Tag.objects.get(pk=etiqueta_id)  #(id=etiqueta_id)
        resultado=Project.objects.filter(tags=etiqueta)
        # print(f"------------------{etiqueta_id}")
        # print(f"------------------{etiqueta}")
        # print(f"------------------{resultado}")
        return resultado

class EtiquetaDetailView(DetailView):
    model = Tag
    template_name = 'proyecto/pruebas.html'
    context_object_name = 'proyectos_por_etiquetas'




# ------ SERIALIZERS -------------
class ProjectListApiView(ListAPIView):
    serializer_class=ProjectSerializer
    def get_queryset(self):
        return Project.objects.all()


class ProjectCreateAPIView(CreateAPIView):
    serializer_class= ProjectSerializer


class ProjectDetailView(RetrieveAPIView):

    serializer_class= ProjectSerializer
    queryset= Project.objects.all() #en vez de all se puede poner el filter

class ProjectDeleteView(DestroyAPIView):

    serializer_class= ProjectSerializer
    queryset= Project.objects.all()

class ProjectUpdateView(UpdateAPIView):

    serializer_class= ProjectSerializer
    queryset= Project.objects.all()

class ProjectRetrieveUpdateAPIView(RetrieveUpdateAPIView):

    serializer_class= ProjectSerializer
    queryset= Project.objects.all() #en vez de all se puede poner el filter


class Project2ApiLista(ListAPIView):
    # serializer_class= PersonaSerializer
    serializer_class= Project2Serializer

    def get_queryset(self):
        return Project.objects.all()


class ProjectApilistaLink(ListAPIView):

    # serializer_class= PersonaSerializer
    serializer_class= ProjectSerializerLink

    def get_queryset(self):
        return Project.objects.all()

class ProjectPaginationList(ListAPIView):

    serializer_class= ProjectSerializer
    pagination_class= PersonPagination

    def get_queryset(self):
        return Project.objects.all()

class ProjectByCategory(ListAPIView):

    serializer_class=CountReunionSerializer
    def get_queryset(self):
        return Project.objects.total_proyecto_categoria()






# ------ SERIALIZERS -------------






#=========PRUEBAS==========

#=========PRUEBAS==========




# #basado en funciones
# def home(request):
#     return render(request,'index.html')

# def add(request):
#     return render(request,'add.html')

# def list(request):
#     return render(request,'list.html')

# # def add2(request):
# #     return render(request,'add2.html')

# def update(request):
#     return render(request,'update.html')

# def delete(request):
#     return render(request,'delete.html')






