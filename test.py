import tensorflow
from keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.layers import GlobalMaxPooling2D
import cv2
import numpy as np
from numpy.linalg import norm
import pickle

#-----------------------------------------




#-------------------------------------------

feature_list=np.array(pickle.load(open("featurevector.pkl","rb")))
filename=pickle.load(open("filenames.pkl","rb"))


model=ResNet50(weights='imagenet',include_top=False,input_shape=(224,224,3))
model.trainable=False




model = tf.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])
model.summary()


def extract_feature(img_path,model):
    img = cv2.imread(img_path)
    img = cv2.resize(img,(224,224))
    img=np.array(img)
                # (number_of_image,224,224,3)
    expand_img=np.expand_dims(img,axis=0)
    pre_img=preprocess_input(expand_img)
    normalized=result/norm(result)
    return normalized