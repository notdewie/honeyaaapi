from rest_framework.response import Response
from server.serializers import PersonSerializer,GetUIDSerializer, PictureSerializer
from server.models import Person, Picture
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
# Create your views here.
