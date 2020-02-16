
This project has the Django source code required to process and store the images recieved from the android application into a local database.

The model is pretrained and loaded.

The model is trained for 3 monuments in Goa 

The Android Application uses Retrofit as the rest API on the client side to communicate with the django server

# The Code For Training The Model(Run In jupyter notebook)::
# importing the libraries

from keras.models import Sequential

from keras.layers import Convolution2D,MaxPooling2D,Flatten,Dropout,Dense

from keras.preprocessing.image import ImageDataGenerator

from keras.callbacks import EarlyStopping , ReduceLROnPlateau

import matplotlib.pyplot as plt

import seaborn as sns

%matplotlib inline

# Image Preprocessing

# ImageDataGenerator is used to create all possible deformation of a given image thereby increasing the dataset

train_data = ImageDataGenerator(rescale = 1./255 , horizontal_flip = True , shear_range = 0.2 , rotation_range = 25 
                                , zoom_range = 0.2 )
                                
val_data = ImageDataGenerator(rescale = 1./255)

# Collection data from the directory of the localhost
# enter the directory from where data is to be fetched in ''

training_set = train_data.flow_from_directory('', target_size = (128,128) , batch_size = 32 , class_mode = 'categorical' )

validation_set = val_data.flow_from_directory('', target_size = (128,128) , batch_size = 32 , class_mode = 'categorical' )

# Model Creation

model = Sequential()

model.add(Convolution2D(32 , (5,5) , activation = 'relu' , input_shape = (128,128,3)))

model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Convolution2D(64 , (3,3) , activation = 'relu'))

model.add(MaxPooling2D(pool_size =(2,2)))

model.add(Convolution2D(64 , (3,3) , activation = 'relu'))

model.add(MaxPooling2D(pool_size =(2,2)))

model.add(Flatten())

model.add(Dense(128 , activation = 'relu'))

model.add(Dropout(0.2))

# Dropout will help reduce Ovevrfitting

model.add(Dense(128 , activation = 'relu'))

model.add(Dropout(0.1))

# 3 is the number of classes expected at the output layer

model.add(Dense(3 , activation = 'softmax'))

model.compile(optimizer = keras.optimizers.RMSprop(lr=0.0001, decay=1e-6) ,loss = 'categorical_crossentropy' , metrics = ['accuracy'])

# Earlystopping will help reduce overfitting
# ReduceLROnPlateau will reduce the learning rate 

result = model.fit_generator(training_set , steps_per_epoch = (training_set.n/training_set.batch_size) , epochs = 30 
                    , validation_data = validation_set , validation_steps = (validation_set.n/validation_set.batch_size)
                    , callbacks = [EarlyStopping(patience = 3 , restore_best_weights = True) , ReduceLROnPlateau(patience = 2)])


# Visualization

acc = model.history['acc']

val_acc = model.history['val_acc']

loss = model.history['loss']

val_loss = model.history['val_loss']

epochs = range(len(acc))

sns.set_style('whitegrid')

plt.figure(figsize = (12,8))

plt.plot(epochs , acc , color = 'red' ,label = 'training Accuracy')

plt.plot(epochs , val_acc , color = 'blue' ,label = 'Validation Accuracy')

plt.title('Training and validation accuracy')

plt.legend()


plt.figure(figsize = (12,8))

plt.plot(epochs , loss , color = 'red' ,label = 'training loss')

plt.plot(epochs , val_loss , color = 'blue' ,label = 'Validation loss')

plt.title('Training and validation loss')

plt.legend()


 

