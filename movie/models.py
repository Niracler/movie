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
    style = models.CharField(max_length=64, verbose_name='制式')
    release_time = models.CharField(max_length=128, verbose_name='上映时间')
    duration = models.CharField(max_length=64, verbose_name='片长')
    movie_type = models.CharField(max_length=64, verbose_name='电影类型')
    director = models.CharField(max_length=256, verbose_name='导演')
    starring = models.CharField(max_length=256, verbose_name='明星')
    production_company = models.CharField(max_length=256, verbose_name='制作公司')
    publish_company = models.CharField(max_length=256, verbose_name='出版公司')
    created = models.DateTimeField(verbose_name='爬取时间')

    class Meta:
        ordering = ('-mid',)
        db_table = "movie"

    def __str__(self):
        return self.name


class MovieBoxOffice(models.Model):
    mid = models.ForeignKey(Movie, models.DO_NOTHING, verbose_name='电影ID')
    week = models.CharField(max_length=64, verbose_name='周数')
    week_time = models.CharField(max_length=128, verbose_name='每周时间')
    average_per_game = models.IntegerField(verbose_name='场均人次')
    one_week_box_office = models.IntegerField(verbose_name='单周票房')
    total_box_office = models.IntegerField(verbose_name='累计票房（万）')
    days_released = models.IntegerField(verbose_name='上映天数')

    class Meta:
        ordering = ('-mid',)
        db_table = "movie_box_office"

    def __str__(self):
        return self.mid