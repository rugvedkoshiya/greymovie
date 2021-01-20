from django.contrib import admin
from .models import MoviePost

# Register your models here.

# class MoviePostAdmin(admin.ModelAdmin):
#     readonly_fields = ['movie_date']

# admin.site.register(MoviePost, MoviePostAdmin)
admin.site.register(MoviePost)