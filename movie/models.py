from django.db import models


# Create your models here.


class Movie(models.Model):
    mid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=65)
    english_name = models.CharField(max_length=128)
    release_year = models.CharField(max_length=16)
    default_image = models.CharField(max_length=256)
    box_office = models.IntegerField()
    area = models.CharField(max_length=128)
    area_id = models.IntegerField()
    ranking = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        ordering = ('-created',)
        db_table = "movie"

    def __str__(self):
        return self.name
