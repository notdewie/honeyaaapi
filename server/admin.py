from django.contrib import admin
from .models import User, Person, SwipePerson

admin.site.register(User)
admin.site.register(Person) 
admin.site.register(SwipePerson)

# Register your models here.
