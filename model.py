# This code imports the necessary libraries to create a voting classifier.
# It imports pandas and numpy for data manipulation, sklearn for train/test split
# tensorflow for the neural network, and keras for the Sequential model, Dense and Dropout layers.
# It also imports the VotingClassifier and accuracy_score from sklearn.


import pandas as pd
# import numpy as np

from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.ensemble import VotingClassifier
# from sklearn.metrics import accuracy_score


# Read an excel file from the specified file path, change the category column from string values to numerical values.
# The code then drops the "NAME" and "Unnamed: 0" columns from our dataframe
# Split our data into Features (X1) and Labels (y1).

df1 = pd.read_excel("Y3_&_Y2_Labelled_Data.xlsx", engine='openpyxl')
df1["Category"] = df1["Category"].map({"Digital Electronics":1,"System Software":2,"Software Engineering":3,"Networking":4})

df1.drop(columns=["NAME", "Unnamed: 0"], inplace=True)

X1 = df1.drop(columns="Category")
y1 = df1["Category"]


# This code creates two models with different layers.
# The first model has 4 layers, the second model has 3 layers.
# The models both use the same optimizer, but different weight decay values.
# The first model uses a weight decay of 0.001 and the second model uses a weight decay of 0.0001.

weight_decay=0.001
weight_decay2=0.0001
def create_model():
    model = Sequential([
        Dense(4, input_shape=(4,), activation='relu'),
        Dense(32, activation='relu'),
        Dense(16, activation='relu'),
        Dense(64, activation='relu'),
        Dense(4, activation='softmax')
    ])
    model.compile(loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True), optimizer=tf.keras.optimizers.Adam(learning_rate=0.001,beta_1=0.9, beta_2=0.999,epsilon=1e-07,amsgrad=False,decay=weight_decay), metrics=['accuracy'])
    return model

def create_model1():
    model1 = Sequential([
        Dense(4, input_shape=(4,), activation='relu'),
        Dense(32, activation='relu'),
        Dense(16, activation='relu'),
        #Dense(64, activation='relu'),
        Dense(4, activation='softmax')
    ])
    model1.compile(loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True), optimizer=tf.keras.optimizers.Adam(learning_rate=0.001,beta_1=0.9, beta_2=0.999,epsilon=1e-07,amsgrad=False,decay=weight_decay2), metrics=['accuracy'])
    return model1

# This code creates three KerasClassifier models, model1, model2, and model3,
# using the function create_model and create_model1.
# Each model is initialized with 200 epochs, a batch size of 40, and verbosity set to 1.

model1 = KerasClassifier(build_fn=create_model, epochs=200, batch_size=40, verbose=1)
model2 = KerasClassifier(build_fn=create_model1, epochs=200, batch_size=40, verbose=1)
model3 = KerasClassifier(build_fn=create_model1, epochs=200, batch_size=40, verbose=1)


# This code sets the estimator type for three different models (model1, model2, model3) to "classifier".
# Then creates an ensemble VotingClassifier from the three models.
# The VotingClassifier is given the parameters 'estimators', which is a list of the three models and their names.

model1._estimator_type = "classifier"
model2._estimator_type = "classifier"
model3._estimator_type = "classifier"
ensemble = VotingClassifier(estimators= [('model1', model1) , ('model2', model2), ('model3', model3)], verbose=True)


'''This code is used to split a dataset into training and test sets. The parameters are:

test_size: The proportion of the dataset to be used for the test set (0.15 in this case)

random_state: The seed used by the random number generator (42 in this case)

stratify: The labels used to stratify the dataset (y1 in this case)'''


X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size=0.15, random_state=42, stratify=y1)


# This code fits an ensemble model, which is a type of supervised learning algorithm, to the training data.
# The ensemble model combines the predictions from multiple models to create a stronger, more accurate model.

ensemble.fit(X_train1, y_train1)



