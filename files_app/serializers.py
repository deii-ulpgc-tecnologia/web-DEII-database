from rest_framework import serializers
from subjects_app.models import Subject
from . models import *
from django.core.exceptions import ValidationError
from .validators import file_size_by_category_validator, extension_whitelist_validator

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['name']
        read_only_fields = ['id', 'tagged_files']

class FilePublicSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    subject_id = serializers.SlugRelatedField(many=True, queryset=Subject.objects.all(), slug_field='name')

    class Meta:
        model = File
        fields = ['id','name', 'subject_id', 'uploader', 'file', 'tags']
        read_only_fields = ['id', 'approved_at']

    def validate_file(self, f):
        try:
            file_size_by_category_validator(f)
            extension_whitelist_validator(f)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return f