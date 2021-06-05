from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField

# class Players (models.Model):
#     #idPlayer = models.TextField(max_length=20)
#     namePlayer = models.TextField(max_length=100)
#     agePlayer = models.IntegerField()

# user table
class User (models.Model):
    userName = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=20)

    def __str__(self):
        return self.userName

# person table
class Person (models.Model):
    personName = models.CharField(max_length=20)

    owner = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True,
    )

    swipePerson = models.ManyToManyField('self', through='SwipePerson', symmetrical=False)
    interested = models.ManyToManyField('Interest')
    oriented = models.ForeignKey('Oriented', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.personName

# Person to Person third table
class SwipePerson (models.Model):
    fromPerson = models.ForeignKey(Person, related_name='from_person' ,on_delete=models.SET_NULL, null=True)
    toPerson = models.ForeignKey(Person, related_name='to_person', on_delete=models.SET_NULL, null=True)

    liked = models.BooleanField()

    def __str__(self):
        return "{} to {}".format(self.fromPerson, self.toPerson)

# Interest table
class Interest (models.Model):
    interestName = models.CharField(max_length=20)

    def __str__ (self):
        return self.interestName

# sex oriented table
class Oriented (models.Model):
    orientedType = models.CharField(max_length = 20)

    def __str__(self):
        return self.orientedType
