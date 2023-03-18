# Sign-Language-Alphabet-dataset-and-prediction
This repository contains a dataset of images for sign language alphabet recognition. The images were created using the Mediapipe library to detect and track the hand landmarks and gestures of individuals forming the sign language alphabets.

## Dataset
The dataset consists of images of hands forming sign language alphabets, captured in real-time using a webcam. The images are organized into folders for each alphabet, with each folder containing images of individuals forming the alphabet in different positions and orientations.#

## Data Collection
The data was collected using the Mediapipe library, which provides a Python API for building and applying various machine learning models for hand tracking and gesture recognition. The library was used to detect and track the landmarks of the hand and generate images of the hand in different orientations and positions.

The data collection script is included in the DataCollection.py, which can be used to capture additional data using a webcam and the Mediapipe library.
## Model
The CNN used for sign language alphabet recognition is implemented in the model.py file. The model consists of multiple convolutional and pooling layers, followed by two fully connected layers. The model is trained on the training set using the Adam optimizer and categorical crossentropy loss. The trained model is then saved in the model directory.

## Prediction
To predict sign language alphabets using the trained model, run the Testing.py script in the root directory of the repository. The script prompts the user to input the path to an image of a hand forming a sign language alphabet. The script then uses the trained model to predict the alphabet in the image.
