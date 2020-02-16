
#---------------DATA INSERTION----------
# The url willbe directed to /uploads where this class will be invoked to do the insertion of data

# Create your views here.
from .serializers import imageSerializer
from rest_framework.generics import (CreateAPIView)
from image_app.models import MyImage
#from .models import MyImage
#from django.shortcuts import render

class ImageCreateAPIView(CreateAPIView):
	serializer_class = imageSerializer
	queryset = MyImage.objects.all()	


