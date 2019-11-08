import django_filters
from .models import Movie


class MovieFiliter(django_filters.rest_framework.FilterSet):
    """电影信息的api的过滤器"""
    mid = django_filters.CharFilter(field_name='mid')
    name = django_filters.CharFilter(field_name='name')
    english_name = django_filters.CharFilter(field_name='english_name')
    release_year = django_filters.CharFilter(field_name='release_year')
    box_office = django_filters.CharFilter(field_name='box_office')
    area = django_filters.CharFilter(field_name='area')
    area_id = django_filters.CharFilter(field_name='area_id')
    ranking = django_filters.CharFilter(field_name='ranking')
    created = django_filters.CharFilter(field_name='created')

    class Meta:
        model = Movie
        fields = [
            'mid', 'name', 'english_name', 'release_year',
            'box_office', 'area', 'area_id', 'ranking', 'created'
        ]
