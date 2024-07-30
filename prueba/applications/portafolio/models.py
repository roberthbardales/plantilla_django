from django.db import models

from .managers import ProyectoManager
class Tag(models.Model):

    name = models.CharField(max_length=200,unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')
    class Meta:

        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering=['name']

    def __str__(self):
        # return self.name
        return str(self.id) + '-' + self.name

class Category(models.Model):

    name = models.CharField(max_length=200,unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated= models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')

    # obejcts=CategoriaManager()
    class Meta:

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering=['name']
    def __str__(self):
        # return self.name
        return str(self.id) + '-' + self.name


class Project(models.Model):

    title = models.CharField(max_length=200,unique=True, verbose_name='Titulo')
    description = models.CharField(max_length=200,unique=True, verbose_name='Descripcion')
    image = models.ImageField(upload_to='Imagen')
    # image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion')
    #relacionados
    tags = models.ManyToManyField(Tag,verbose_name='Etiquetas')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Categoria')
    #Conectar con el manager
    objects= ProyectoManager()

    def __str__(self):
        # return self.name
        return str(self.id) + '-' + self.title