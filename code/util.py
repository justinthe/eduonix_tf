import os
from os.path import join, isdir
import tensorflow as tf
from skimage import transform
from skimage import data

def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory)
            if os.path.isdir(os.path.join(data_directory, d))]

    labels = []
    images = []
    for d in direcotries:
        label_direcotry = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f) for f in os.listdir(label_directory) if f.endswith(".ppm")]
        for f in file_names:
            images.append(data.imread(f))
            labels.append(int(d))
    return images, labels

ROOT_PATH = "./"
train_data_directory = os.path.join(ROOT_PATH, "TrafficSigns/Training")
test_data_directory = os.path.join(ROOT_PATH, "TrafficSigns/Testing")
images, labels = load_data(train_data_directory)
