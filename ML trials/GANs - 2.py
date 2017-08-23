import os
import numpy as np
from scipy.misc import imread
from tqdm import tqdm
import cv2
import matplotlib.pyplot as plt

import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Reshape, InputLayer
from keras.regularizers import L1L2

from keras_adversarial import AdversarialModel, simple_gan, gan_targets
from keras_adversarial import AdversarialOptimizerSimultaneous, normal_latent_sampling



g_input_shape=5000
d_input_shape=(100,100)

hidden_1_num_units=8000
hidden_2_num_units=8000

g_output_num_units=10000
d_output_num_units=1

epochs=25
batch_s=128


model_G = Sequential([
    
    Dense(units=hidden_1_num_units,
          input_dim=g_input_shape,
          activation='relu',
          kernel_regularizer=L1L2(1e-5,1e-5)),
    
    Dense(units=hidden_2_num_units,
          activation='relu',
          kernel_regularizer=L1L2(1e-5,1e-5)),
    
    Dense(units=g_output_num_units,
          activation="sigmoid",
          kernel_regularizer=L1L2(1e-5,1e-5)),
    
    Reshape(d_input_shape),            
    ])


model_D=Sequential([
    InputLayer(input_shape=d_input_shape),
    Flatten(),
    
    Dense(units=hidden_1_num_units,
          activation='relu',
          kernel_regularizer=L1L2(1e-5,1e-5)),
    
    Dense(units=hidden_2_num_units,
          activation='relu',
          kernel_regularizer=L1L2(1e-5,1e-5)),
    

    Dense(units=d_output_num_units, 
           activation='sigmoid', 
           kernel_regularizer=L1L2(1e-5, 1e-5)),

    ])


path="F:/Data/CatsVsDogs/train"

temp=[]
for img_name in tqdm(os.listdir(path)):
    if img_name.split(".")[0]=="dog":
        image_path=os.path.join(path,img_name)
        img=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
#        cv2.imshow("Window",img)
#        cv2.waitKey(2)
        img=cv2.resize(img,(100,100))
        img=np.asarray(img)
        temp.append(img)


train_x= np.stack(temp)


cv2.imshow("Window",temp[5][:])
cv2.waitKey(0)

gan= simple_gan(model_G, model_D, normal_latent_sampling((5000,)) )

model = AdversarialModel(base_model=gan,player_params=[model_G.trainable_weights, model_D.trainable_weights])

model.adversarial_compile(adversarial_optimizer=AdversarialOptimizerSimultaneous(), 
                          player_optimizers=['adam', 'adam'], 
                          loss='binary_crossentropy')

history=model.fit(x=train_x, y=gan_targets(train_x.shape[0]), epochs=100, batch_size=batch_s)



plt.plot(history.history['player_0_loss'])
plt.plot(history.history['player_1_loss'])
plt.plot(history.history['loss'])



zsamples = np.random.normal(size=(10, 500))
pred = model_G.predict(zsamples)
for i in range(pred.shape[0]):
    img=pred[i,:]
    img=cv2.resize(img,(200,200))
    cv2.imshow("Image",img)
    cv2.waitKey(1000)