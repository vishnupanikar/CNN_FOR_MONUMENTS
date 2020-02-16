# Register your models here.

# The databases to be used are to be created first..
# Here the Database is registered
# Refering to Database , I mean the tables
from django.contrib import admin
from image_app.models import MyImage


admin.site.register(MyImage)
