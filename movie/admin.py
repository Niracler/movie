from django.contrib import admin
from .models import Movie


# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('mid', 'name', 'english_name' , 'box_office', 'area_id', 'area', 'created')
