#-------------------------------------MAIN LOGIC------------------------------

from image_app.models import MyImage
# This is the image_app folder containing the Database named as My Image which is stored by django as image_app_myimage

from django.shortcuts import render
# render is a function that is used to send The Http response 
# here the response is send to the Current Page , as specified in the urls.py in the imageproject

from keras.models import load_model
from keras.preprocessing import image
import numpy as np


def output(request):
      print("hello")
      obj = MyImage.objects.all()
      n = len(obj)
      # here the obj will be a Queryset(iterable)
      # Querryset contains list of objects
      # Each Object is a dictionary 
      # The Keys represent the Attribute and value is the value related to that attribute

      test_image = obj[n-1].model_pic.url
      # test_image will be containing the directory of the folder where the image is stored 
      # here we acccess one object from list of objects 
      # and each object is an entry in the database 
      # .url will give the path of the selected attribute of the object(here In This Case It is the image)

      goa_cnn = load_model('cifar_colab.h5')

      print(test_image)
      # For seeing the directory of selected image
      

      #This is to test one image
      #as my reqirement is to test one image clicked at a time

      test_image = image.load_img('D:/django-project/imageproject'+test_image , target_size = (32,32))
      #the full image directory is needed so the string returned by the test_image is concatenated 
      #for cifar the standard Input for the model is 32x32.
      test_image = image.img_to_array(test_image)
      test_image = np.expand_dims(test_image , axis = 0)

      classes = {0:"Airplane" , 1:"Automobile" , 2:'Bird' , 3:'Cat' , 4:'Deer' , 5:'Dog' , 6:'Frog' , 7:'Horse', 8:'Ship' , 9:'Truck'}
      #class2 = {0:'Aguada Fort Lighthouse' , 1:'Basilica Of Bom Jesus' , 2:'St. Cajetan'}


      result_class = goa_cnn.predict_classes(test_image)
      print('Class :: ',result_class[0])
      data = classes[result_class[0]]

      return render(request , 'home.html' ,{'data' : data})
      #This returns the result of the prediction to home.html 
      #the data to be sent is madded into dictonary format

      