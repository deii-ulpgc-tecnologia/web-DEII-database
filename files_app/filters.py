import django_filters
from .models import File
from subjects_app.models import SemesterEnum, YearEnum

class FilePublicFilter(django_filters.FilterSet):
    degree = django_filters.CharFilter(field_name="subject_id__degree__name")
    year = django_filters.ChoiceFilter(choices=YearEnum,field_name="subject_id__year")
    semester = django_filters.ChoiceFilter(choices=SemesterEnum.choices,field_name="subject_id__semester")
    area = django_filters.CharFilter(field_name="subject_id__area__name")

    class Meta:
        model = File
        fields = ["year", "degree", "semester", "area"]