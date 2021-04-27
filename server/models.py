from django.db import models

class Players (models.Model):
    #idPlayer = models.TextField(max_length=20)
    namePlayer = models.TextField(max_length=100)
    agePlayer = models.IntegerField()
