# Testing the Tensorflow Server with Fashion MNIST model
# This program was tested with tensorflow version 2.3.0

# Necessary libraries
from tensorflow import keras
import numpy as np
import requests
import json

# Load the fashin MNIST datast, but specifically the test images and labels
fashion_mnist = keras.datasets.fashion_mnist
(test_images, test_labels) = fashion_mnist.load_data()[1]

# scale the values to 0.0 to 1.0 and reshape (necessary to test the served model)
test_images = test_images / 255.0
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

# for converting labels to class names
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Print the shape
print('test_images.shape: {}, of {}\n\n'.format(test_images.shape, test_images.dtype))


# Testing a Single request with the name of the model
print ('Testing A single Request')
data = json.dumps({"signature_name": "serving_default", "instances": test_images[0:3].tolist()})
print('Data: {} ... {}\n\n'.format(data[:50], data[len(data)-52:]))

# prepare headers and json request
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/fashion_mnist:predict', data=data, headers=headers)
predictions = json.loads(json_response.text)['predictions']

# Print ground truth vs predictions
print('Ground Truth = {} class {}, Prediction = {} class {}\n\n'.format(
	class_names[np.argmax(predictions[0])], test_labels[0], 
	class_names[np.argmax(predictions[0])], test_labels[0]))


# Testing on Multiple request and a specific model, for example version 1, 2, 3 and so on.
# Actually we only have 1 version of the model so it will be 1
print ('Testing multiple requests')
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/fashion_mnist/versions/1:predict', data=data, headers=headers)
predictions = json.loads(json_response.text)['predictions']

for i in range(0,3):
  print('Ground Truth = {} class {}, Prediction = {} class {}'.format(
    class_names[np.argmax(predictions[i])], np.argmax(predictions[i]), 
    class_names[test_labels[i]], test_labels[i]))