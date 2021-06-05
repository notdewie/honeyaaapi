from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField

# class Players (models.Model):
#     #idPlayer = models.TextField(max_length=20)
#     namePlayer = models.TextField(max_length=100)
#     agePlayer = models.IntegerField()

class User (models.Model):
    userName = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=20)

    def __str__(self):
        return self.userName

class Person (models.Model):
    personName = models.CharField(max_length=20)

    owner = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True,
    )



    def __str__(self):
        return self.personName
