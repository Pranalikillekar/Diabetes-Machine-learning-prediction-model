# -*- coding: utf-8 -*-
"""Copy of Project 3 - Diabetes Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XscEeehFSiecy3nB8cUgDEnwY9DAS0Dm

Importing the Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and Analysis

PIMA Diabetes Dataset
"""

# loading the diabetes dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv('/content/diabetes.xls - diabetes.csv')

pd.read_csv?

# printing the first 5 rows of the dataset
diabetes_dataset.head()

# number of rows and Columns in this dataset
diabetes_dataset.shape

# getting the statistical measures of the data
diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""0 --> Non-Diabetic

1 --> Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

# separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']

print(X)

print(Y)

"""Data Standardization"""

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

print(X)
print(Y)

"""Train Test Split"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Training the Model"""

classifier = svm.SVC(kernel='linear')

#training the support vector Machine Classifier
classifier.fit(X_train, Y_train)

"""Model Evaluation

Accuracy Score
"""

# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy score of the training data : ', training_data_accuracy)

# accuracy score on the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score of the test data : ', test_data_accuracy)

"""Making a Predictive System"""

input_data = (5,166,72,19,175,25.8,0.587,51)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the diabetes dataset
diabetes_dataset = pd.read_csv('/content/diabetes.xls - diabetes.csv')

# Separate features and labels
X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']

# Standardize the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train the SVM classifier
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Evaluate the model
Y_pred = classifier.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print('Accuracy:', accuracy)
print('Classification Report:\n', classification_report(Y_test, Y_pred))
print('Confusion Matrix:\n', confusion_matrix(Y_test, Y_pred))

# Bar graph of prediction counts
prediction_counts = pd.Series(Y_pred).value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=prediction_counts.index, y=prediction_counts.values)
plt.title('Prediction Counts')
plt.xticks([0, 1], ['Non-Diabetic', 'Diabetic'])
plt.xlabel('Predicted Outcome')
plt.ylabel('Count')
plt.show()

#Bar graph of actual counts.
actual_counts = pd.Series(Y_test).value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=actual_counts.index, y=actual_counts.values)
plt.title('Actual Outcome Counts')
plt.xticks([0, 1], ['Non-Diabetic', 'Diabetic'])
plt.xlabel('Actual Outcome')
plt.ylabel('Count')
plt.show()

#Feature importance (approximation for linear SVM):
if classifier.kernel == 'linear':
    feature_importance = np.abs(classifier.coef_[0])
    feature_names = diabetes_dataset.drop('Outcome', axis=1).columns
    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
    feature_importance_df = feature_importance_df.sort_values('Importance', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
    plt.title('Feature Importance (Linear SVM)')
    plt.show()
else:
    print("Feature importance is not directly available for non-linear SVM kernels.")