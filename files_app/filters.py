import django_filters
from .models import File

class FilePublicFilter(django_filters.FilterSet):
    s_year = django_filters.NumberFilter(field_name="subject_id__year")
    s_degree = django_filters.CharFilter(field_name="subject_id__degree")
    s_semester = django_filters.NumberFilter(field_name="subject_id__semester")
    s_area = django_filters.CharFilter(field_name="subject_id__area")

    class Meta:
        model = File
        fields = ["s_year", "s_degree", "s_semester", "s_area"]