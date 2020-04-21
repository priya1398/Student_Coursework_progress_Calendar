from django.contrib import admin

# Register your models here.
from .models import BookList,Event

admin.site.register(BookList)
admin.site.register([Event])