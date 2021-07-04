from re import X
from django.db.models.fields.related import ManyToManyField
from rest_framework import response
from rest_framework.response import Response
from server.serializers import PersonSerializer,GetUIDSerializer, PictureSerializer, SwipePersonSerializer
from server.models import Interest, Person, Picture, SwipePerson
from django.shortcuts import render
from rest_framework.views import APIView

class getinfo(APIView):
    def get (self,request, uid ):
        person = Person.objects.filter(uid = uid)
        serial = GetUIDSerializer(person, many = True)
        return Response(serial.data)

class getpicture(APIView):
    def get(sefl, request, uid):
        picture = Picture.objects.filter(owner__id__contains = uid)
        serial = PictureSerializer(picture, many = True)
        return Response(serial.data)

class getlikedpersion(APIView):
    def get(self, request, uid):
        likedperson = Person.objects.raw('SELECT * FROM server_person Join server_swipeperson On server_person.id = server_swipeperson."fromPerson_id" WHERE server_swipeperson."toPerson_id" = ' + uid)
        # likedperson = Person.objects.filter(from_person__liked = True).exclude(id = uid).filter(swipePerson__toPerson__id = uid)
        # likedperson = Person.objects.filter(from_person__liked = True).exclude(id = uid).filter(from_person__toPerson__id = uid)
        serial = GetUIDSerializer(likedperson, many = True)
        # serial = PersonSerializer(likedperson, many = True, context={'request': request})
        return Response(serial.data)

class getlike(APIView):
    def get(self, request, uid):
        likedperson = Person.objects.raw('SELECT * FROM server_person Join server_swipeperson On server_person.id = server_swipeperson."fromPerson_id" WHERE server_swipeperson."toPerson_id" = ' + uid)
        serial = PersonSerializer(likedperson, many = True, context={'request': request})
        return Response(serial.data)


class getswipeperson(APIView):
    def get(self, request, uid):
        person = Person.objects.all()
        serial = PersonSerializer(person, many = True)
        return Response(serial.data)

class swipe(APIView):
    def get(self, request, uid):
        id = 5
        person = Person.objects.raw('SELECT * FROM server_person')
        serial = PersonSerializer(person, many = True,context={'request': request}) 
        # swipe = SwipePerson.objects.filter(fromPerson__id = id)

        # swipe = SwipePerson.objects.raw(
        #     'SELECT * \
        #     FROM server_swipeperson \
        #         INNER JOIN server_swipeperson as LikeMe\
        #             ON server_swipeperson.fromPerson_id = LikeMe.toPerson_id\
        #     WHERE server_swipeperson.'
        # )
        

        # serial = SwipePersonSerializer(swipe, many = True, context={'request': request})
        return Response(serial.data)


# select UserLikes.ShownUserId 
# from UserLikes
#     inner join UserLikes as AlsoLikesMe
#         on UserLikes.UserId = AlsoLikesMe.ShownUserId
#             and AlsoLikesMe.Liked = yes
# where UserLikes.UserId = 'John' and UserLikes.Liked = yes
# Create your views here.
