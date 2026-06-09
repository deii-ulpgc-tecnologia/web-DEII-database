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

class FileListSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    subjects = serializers.SlugRelatedField(many=True, read_only=True, slug_field='combined_abbreviation')

    class Meta:
            model = File
            fields = ['id', 'name', 'extension', 'subjects', 'tags']
            read_only_fields = ['id', 'name', 'extension']

class FilePublicSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    subjects = serializers.SlugRelatedField(many=True, queryset=Subject.objects.all(), slug_field='name')

    class Meta:
        model = File
        fields = ['id', 'name', 'subjects', 'uploader', 'file', 'tags', 'approved_at']
        read_only_fields = ['id', 'approved_at']

    def validate_file(self, f):
        try:
            file_size_by_category_validator(f)
            extension_whitelist_validator(f)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return f

class FilePrivateListSerializer(serializers.ModelSerializer):
    subjects = serializers.SlugRelatedField(many=True, read_only=True, slug_field='combined_abbreviation')
    status_display = serializers.CharField(read_only=True, source='get_status_display')

    class Meta:
        model = File
        fields = ['id', 'name', 'extension', 'subjects', 'status_display']
        read_only_fields = ['id', 'name', 'extension', 'status_display']

class FilePrivateSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, queryset=Subject.objects.all(), slug_field='name')
    subjects = serializers.SlugRelatedField(many=True, queryset=Subject.objects.all(), slug_field='name')
    status_display = serializers.CharField(read_only=True, source='get_status_display')

    class Meta:
        model = File
        fields = ['id', 'name', 'file', 'extension', 'subjects', 'tags', 'uploader', 'uploaded_at', 'status_display',
                  'approved_by', 'approved_at']
        read_only_fields = ['id', 'file', 'extension', 'uploader', 'uploaded_at', 'status_display',
                            'approved_by', 'approved_at']