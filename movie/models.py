from django.db import models


# Create your models here.


class Movie(models.Model):
    mid = models.IntegerField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=65, verbose_name='电影名称')
    english_name = models.CharField(max_length=128, verbose_name='英文名称')
    release_year = models.CharField(max_length=16, verbose_name='发行年限')
    default_image = models.CharField(max_length=256, verbose_name='图片')
    box_office = models.IntegerField(verbose_name='票房')
    area = models.CharField(max_length=128, verbose_name='地区')
    area_id = models.IntegerField(verbose_name='地区号')
    ranking = models.IntegerField(verbose_name='排名')
    created = models.DateTimeField(verbose_name='爬取时间')

    class Meta:
        db_table = "movie"

    def __str__(self):
        return self.name
