#----------------DATABASE CREATION-------------
#Every Database created is a subclass of class models.Model

from django.db import models
from django.contrib.auth.models import User

# Here Myimage is the Database name
# model_pic is the column(attribute) name
#ImageField specifies that the datatype of the attribute model_pic is a image 
class MyImage(models.Model):
	model_pic = models.ImageField(upload_to = '' ,  default = 'none/no-img.jpg')
