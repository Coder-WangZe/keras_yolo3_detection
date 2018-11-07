import numpy as np
import tensorflow as tf
from keras.models import Model
from keras.utils import to_categorical
from keras.layers import Input, Conv2D, BatchNormalization, MaxPool2D, Dense, Flatten, activations, Dropout
from keras.preprocessing.image import ImageDataGenerator, img_to_array
from keras.optimizers import adam
from sklearn.utils import shuffle
import os
import cv2


def load_data(train_image_path, shape):
    data = []
    labels = []
    hat_path = train_image_path + "/hat"
    nohat_path = train_image_path + "/no_hat"
    hat_image_dirs = [hat_path + "/" + image_dir for image_dir in os.listdir(hat_path)]
    nohat_image_dirs = [nohat_path + "/" + image_dir for image_dir in os.listdir(nohat_path)]
    for i, hat_image_dir in enumerate(hat_image_dirs):
        image = cv2.imread(hat_image_dir)
        image = cv2.resize(image, (shape[0], shape[1]))
        data.append(image)
        labels.append(1)
    for j, nohat_image_dir in enumerate(nohat_image_dirs):
        image = cv2.imread(nohat_image_dir)
        image = cv2.resize(image, (shape[0], shape[1]))
        data.append(image)
        labels.append(0)

    datas = np.array(data, dtype='float32')
    labels = np.array(labels)
    labels = to_categorical(labels, 2)
    datas, labels = shuffle(datas, labels)
    print("load data successfully !")
    return datas, labels


def build_model(input_shape):
    X = Input(input_shape)
    # bn1 = BatchNormalization(axis=-1)(X)
    conv1 = Conv2D(filters=16, kernel_size=[3, 3], strides=[1, 1], padding="SAME", activation='relu')(X)
    # pool1 = MaxPool2D(pool_size=[2, 2], strides=[2, 2], padding="VALID")(conv1)

    conv2 = Conv2D(filters=32, kernel_size=[3, 3], strides=[2, 2], padding="SAME", activation='relu')(conv1)
    conv3 = Conv2D(filters=64, kernel_size=[3, 3], strides=[2, 2], padding="SAME", activation='relu')(conv2)
    # pool1 = MaxPool2D(pool_size=[2, 2], strides=[2, 2], padding="VALID")(conv3)

    flatten = Flatten()(conv3)
    dropout = Dropout(0.5)(flatten)
    dense1 = Dense(512, activation='relu')(dropout)
    # dense2 = Dense(64, activation='relu')(dense1)
    pred = Dense(2, activation="softmax")(dense1)

    return Model(inputs=X, outputs=pred)


# input image shape
shape = [120, 120]
train_image_path = 'D:\\project3\\chef_hats\\hat_classfier\\train_image\\'

data, label = load_data(train_image_path, shape)
model = build_model((shape[0], shape[1], 3))

opt = adam(lr=0.00001)
model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
# model.fit(x=data, y=label, batch_size=64, epochs=50, verbose=1, validation_split=0.2, shuffle=True)

datagen = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
                             height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
                             horizontal_flip=True, fill_mode="nearest")

model.fit_generator(datagen.flow(data[:800], label[:800], batch_size=64), epochs=50, verbose=1, shuffle=True,
                    validation_data=(data[800:], label[800:]))
