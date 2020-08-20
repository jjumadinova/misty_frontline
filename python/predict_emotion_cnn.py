`https://www.kaggle.com/shawon10/facial-expression-detection-cnn/notebook`
import tensorflow as tf

import keras

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from keras.preprocessing import image


model = tf.keras.models.load_model("model/model_filter.h5")
objects = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

def emotion_analysis(emotions):
    objects = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, emotions, align='center', alpha=0.9)
    plt.tick_params(axis='x', which='both', pad=10,width=4,length=10)
    plt.xticks(y_pos, objects)
    plt.ylabel('percentage')
    plt.title('emotion')



def predict_emotion(face):
    img = image.load_img(face, grayscale=True, target_size=(48, 48))
    show_img=image.load_img(face, grayscale=False, target_size=(200, 200))
    # img = img.reshape([48, 48])
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    y = np.copy(x)
    y //= 255
    # np.true_divide(y, 255, out=y)
    custom = model.predict(x)
    emotion_analysis(custom[0])
    y = np.array(y, 'float32')
    y = x.reshape([48, 48]);

    plt.gray()
    plt.imshow(show_img)
    plt.show()

    m=0.000000000000000000001
    a=custom[0]
    for i in range(0,len(a)):
        if a[i]>m:
            m=a[i]
            ind=i

    print('Expression Prediction:',objects[ind])
