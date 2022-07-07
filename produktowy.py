import numpy as np 
import matplotlib.pyplot as plt
import cv2
import os
from keras.applications.vgg16 import VGG16
import joblib
import pandas as pd
from skimage import measure, io, img_as_ubyte
from skimage.color import label2rgb, rgb2gray
from skimage.filters import threshold_otsu, threshold_local,threshold_minimum




SIZE = 128
VGG_model = VGG16(weights='imagenet', 
                    include_top=False, 
                    input_shape=(SIZE, SIZE, 3))
model = joblib.load('lgb.pkl')
dict1 = {0: 'niemetaliczne_wtrącenie', 
        1: 'otwór',
        2: 'plama_oleju',
        3: 'pofałdowanie',
        4: 'pół_okrągła_nieciągłość',
        5: 'porowatość',
        6: 'spaw',
        7: 'wada_walcowania',
        8: 'wypłukanie',
        9: 'złuszczenie'}

def estimate_prop(i):
    image = img_as_ubyte(rgb2gray(io.imread('pic'+os.sep+files[i])))
    threshold = threshold_minimum(image)
    label_image = measure.label(image < threshold, connectivity=image.ndim)
    plt.imshow(label_image)
    image_label_overlay = label2rgb(label_image, image=image)
    plt.imshow(image_label_overlay)
    plt.show()
    props = measure.regionprops_table(label_image, image, 
                          properties=['label',
                                      'area', 'equivalent_diameter',
                                      'mean_intensity', 'solidity', 'bbox'])

    df = pd.DataFrame(props)
    df=df.sort_values(by=['area'], ascending=False)
    print(df.head())

files=os.listdir("pic")
images2=[]
for i in range(0,len(files)):
    img_path2='pic'+os.sep+files[i]
    img = cv2.imread(img_path2, cv2.IMREAD_COLOR)       
    img = cv2.resize(img, (SIZE, SIZE))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    images2.append(img)
for i in range(0, len(files)):
    input_img = np.expand_dims(images2[i], axis=0)
    input_img_feature=VGG_model.predict(input_img)
    input_img_features=input_img_feature.reshape(input_img_feature.shape[0], -1)
    prediction_RF = model.predict(input_img_features)[0] 
    print("Predykcja: ", dict1[prediction_RF])
    plt.imshow(images2[i])
    plt.show()
    estimate_prop(i)
    plt.show()
