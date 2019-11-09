from rest_framework import serializers
from .models import Movie, MovieBoxOffice


class MovieSerializer(serializers.ModelSerializer):
    """关于电影信息的序列化对象"""

    class Meta:
        model = Movie
        fields = "__all__"


class MovieBoxOfficeSerializer(serializers.ModelSerializer):
    """关于电影票房的序列化对象"""

    class Meta:
        model = MovieBoxOffice
        fields = "__all__"
