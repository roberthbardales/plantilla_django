from django.db import models

from django.db. models import Count


from django.db.models import Q
from django.contrib.postgres.search import TrigramSimilarity



class ProyectoManager(models.Manager):

   def buscar_proyecto_titulo(self,kword_obtenido):
        resultado=self.filter(
            title__icontains=kword_obtenido,
            ).order_by('title')
        return resultado

   def buscar_proyecto_categoria(self,kword_obtenido):
        resultado=self.filter(
            category__name__icontains=kword_obtenido,
            ).order_by('-category')
        print(f"//////////////{resultado}")
        return resultado


   def buscar_proyecto_general(self,kword_obtenido):
        resultado=self.filter(
            Q(title__icontains=kword_obtenido,) |
            Q(description__icontains=kword_obtenido,) |
            Q(category__name__icontains=kword_obtenido,),
            ).order_by('id').distinct()
        return resultado
   def total_proyecto_categoria(self):
        resultado=self.values('category__name').annotate(
            total=Count('id')
            )
        print("********************************************")
        print(resultado)
        return resultado










