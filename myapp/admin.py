from django.contrib import admin
from .models import Actor, Movie,Comment

admin.site.register([Movie,Actor, Comment])