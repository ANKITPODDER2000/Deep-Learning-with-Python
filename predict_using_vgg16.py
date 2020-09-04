# -*- coding: utf-8 -*-
"""predict_using_vgg16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1azoIOuNDlHfVbUJ_SoDYKcMKF6bKNFts
"""

!pip install tensorflow-gpu

import tensorflow as tf
import numpy as np

model = tf.keras.applications.vgg16.VGG16(weights = "imagenet")

# Commented out IPython magic to ensure Python compatibility.
img = tf.keras.utils.get_file("img10.jpg","https://images.theconversation.com/files/258709/original/file-20190213-181593-16pbmxa.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=1200.0&fit=crop")
img = tf.keras.preprocessing.image.load_img(img , target_size=(224 , 244))
img

img_ = tf.keras.preprocessing.image.img_to_array(img)
print(img_.shape)
img__ = img_[np.newaxis , :]
print(img__.shape)

import matplotlib.pyplot as plt
# %matplotlib inline
plt.imshow((img__[0] / 255))

img__ = tf.keras.applications.vgg16.preprocess_input(img__)
pred = model.predict(img__)

print('Predicted:', tf.keras.applications.vgg16.decode_predictions(pred, top=3)[0])

