from rest_framework import serializers

from subjects_app.models import Subject
from . models import *

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['name']
        read_only_fields = ['id', 'tagged_files']

class FilePublicSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    subject_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Subject.objects.all())

    class Meta:
        model = File
        fields = ['id','name', 'subject_id', 'uploader', 'file', 'tags']
        read_only_fields = ['id', 'approved_at']

