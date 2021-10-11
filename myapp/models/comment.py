from django.contrib.auth import get_user_model
from django.db import models
from .movie import Movie

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.CharField(max_length=512)
    created_date = models.DateField(auto_now_add=True)