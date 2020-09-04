# Training and Serving a Model with Tensorflow Serving


# Importing libraries
from tensorflow import keras
import tensorflow as tf
import numpy as np
import tempfile
import os

# I used TF version 2.3.0
print(tf.__version__)

# Create a simple model by Fashion MNIST
# You can read more of the fashion MNIST on the web. It is a replacement of the famous MNIST Digit Dataset. The reason to use fashion MNIST is because it gives better results and also is the "Hello World" of Machine Learning/Deep Learning.

# Load the fashion MNIST Dataset
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# scale the values to 0.0 to 1.0
train_images = train_images / 255.0
test_images = test_images / 255.0

# reshape for feeding into the model
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print('\ntrain_images.shape: {}, of {}'.format(train_images.shape, train_images.dtype))
print('test_images.shape: {}, of {}'.format(test_images.shape, test_images.dtype))


# Train and Evaluate The Model
# Simple model creation
model = keras.Sequential([
  keras.layers.Conv2D(input_shape=(28,28,1), filters=8, kernel_size=3, 
                      strides=2, activation='relu', name='Conv1'),
  keras.layers.Flatten(),
  keras.layers.Dense(10, activation=tf.nn.softmax, name='Softmax')
])
model.summary()

testing = False
epochs = 5

model.compile(optimizer=tf.optimizers.Adam(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=epochs)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('\nTest accuracy: {}'.format(test_acc))

# Saving the Model
# We first need to save the model in the SaveModel format, a .pbtxt and a .pb file that are necessary for tensorflow serving to work
# Fetch the Keras session and save the model
# The signature definition is defined by the input and output tensors,
# and stored with the default serving key

MODEL_DIR = tempfile.gettempdir()
version = 1
export_path = os.path.join(MODEL_DIR, str(version))
print('export_path = {}\n'.format(export_path))

tf.keras.models.save_model(
    model,
    export_path,
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None
)

print('\nSaved model:')
print(os.listdir(export_path))

# Examine if the model generated correctly
#!saved_model_cli show --dir {export_path} --all
# Or upload the .pb file to: https://lutzroeder.github.io/netron/ 