from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """关于电影信息的序列化对象"""

    class Meta:
        model = Movie
        fields = "__all__"
