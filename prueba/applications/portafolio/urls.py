from django.contrib import admin
from django.urls import path
from . import views

from .import views

app_name = "portafolio_app"
urlpatterns = [

 path(
        '',
        views.PaginaInicio.as_view(),
        name="home"
    ),
  path(
        'listar_proyecto/',
        views.ListarProyecto.as_view(),
        name="listar_proyecto"
    ),
    path(
        'detalle_proyecto/<pk>',
        views.ProyectoDetailView.as_view(),
        name="detalle_proyecto"
    ),
    path(
        'agregar_proyecto/',
        views.ProyectoCreateView.as_view(),
        name="agregar_proyecto"
    ),
    path(
        'eliminar_proyecto/<pk>',
        views.ProyectoDeleteView.as_view(),
        name="eliminar_proyecto"
    ),
    path(
        'modificar_proyecto/<pk>',
        views.ProyectoUpdateView.as_view(),
        name="modificar_proyecto"
    ),
    path(
        'buscar_proyecto/',
        views.ListarProyectoByKword.as_view(),
        name='buscar_proyecto',
    ),
# ---------------PRUEBAS INICIO-----------------------
    path(
        'proyecto_etiqueta/<int:etiqueta_id>/',
        views.ProyectosPorEtiquetaListView.as_view(),
        name='proyectos_por_etiqueta'
    ),
    path('etiqueta/<int:pk>/',  #    path('etiqueta/<pk>/',
         views.EtiquetaDetailView.as_view(),
         name='etiqueta_detail'),

# ---------------PRUEBAS FIN-----------------------
# ----------------SERIALIZERS------------------
    path(
        'api/project/lista/',
        views.ProjectListApiView.as_view(),
        name='project_list'
    ),
    path(
        'api/project/create/',
        views.ProjectCreateAPIView.as_view(),
        name='project_create'
    ),
    path(
        'api/project/detail/<pk>/',
        views.ProjectDetailView.as_view(),
        name='project_detail'
    ),
    path(
        'api/project/delete/<pk>/',
        views.ProjectDeleteView.as_view(),
        name='project_delete'
    ),
    path(
        'api/project/update/<pk>/',
        views.ProjectUpdateView.as_view(),
        name='project_update'
    ),
    path(
        'api/project/modificar/<pk>/',
        views.ProjectRetrieveUpdateAPIView.as_view(),
        name='project_modificar'
    ),
    path(
        'api/proyectos2/',
        views.Project2ApiLista.as_view(),
        name='api_proyectos2'
    ),
    path(
        'api/tag_link/',
        views.ProjectApilistaLink.as_view(),
        name='api_tag_link'
    ),
    path(
        'api/proyectos/paginacion/',
        views.ProjectPaginationList.as_view(),
        name=''
    ),
        path(
        'api/totalbycategoria/',
        views.ProjectByCategory.as_view(),
        name=''
    ),




]



#     path(
#         'autores',
#         views.ListarAutores2.as_view(),
#         name="autores"
#     ),
#     path(
#         'buscar-autores/',
#         views.BuscarAutor.as_view(),
#         name="buscar-autores"
#     ),









    # basado en funciones
    # path('',views.home,name='home'),
    # path('add',views.add,name='add'),
    # path('list',views.list,name='list'),
    # # path('add2',views.add2,name='add2'),
    # path('update',views.update,name='update'),
    # path('delete',views.delete,name='delete'),