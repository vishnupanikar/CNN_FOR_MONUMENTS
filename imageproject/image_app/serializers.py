from rest_framework import serializers
# serializer class converts the model into json format

from rest_framework.serializers import (
      ModelSerializer,
)
# ModelSerializer is used to inform the serializer class what is to be serialized,in this case Model

from image_app.models import MyImage
#importing the Database Model

class imageSerializer(ModelSerializer):
   class Meta:
      model = MyImage
      fields = [
         'model_pic'        
      ]
# The attributes specified in the fields are going to be displayed whenever a client requests for data
# The attributes not present in fields will be hidden from the client
