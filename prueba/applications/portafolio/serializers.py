from rest_framework import serializers, pagination

from .models import Project,Tag,Category

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=(
            'id',
            'title',
            'description',
            'image',
            'tags',
            'category',
        )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'active', 'created', 'updated']

class Project2Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    image = serializers.CharField()
    tags = TagSerializer(many=True)  # Utilizar el serializador de Tag
    category = serializers.CharField()
    status = serializers.BooleanField(required=False)  #default=False


class ProjectSerializerLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=Project
        fields=(
            'id',
            'title',
            'description',
            'image',
            'tags',
            # 'category',
        )
        extra_kwargs={
            'tags':{'view_name':'portafolio_app:project_detail','lookup_field':'pk'}
        }

class PersonPagination(pagination.PageNumberPagination):
    page_size=3
    max_page_size=50

class CountReunionSerializer(serializers.Serializer):
    category__name=serializers.CharField()
    total=serializers.IntegerField()