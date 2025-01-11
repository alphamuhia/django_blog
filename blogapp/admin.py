from django.contrib import admin
from .models import Blog, Author, Subscriber

admin.site.register(Blog)
admin.site.register(Author) 
admin.site.register(Subscriber)

