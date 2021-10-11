from django.db import models

class Actor(models.Model):
    GENDER = [
        ("ERKAK", "Erkak"),
        ("AYOL", "Ayol"),
    ]
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER, default="ERKAK")

    def __str__(self):
        return self.name