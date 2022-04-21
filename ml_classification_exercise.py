# The Iris dataset is referred to as a “toy dataset” because it has only 150 samples and four features. 
# The dataset describes 50 samples for each of three Iris flower species—Iris setosa, Iris versicolor and Iris 
# virginica. Each sample’s features are the sepal length, sepal width, petal 
# length and petal width, all measured in centimeters. The sepals are the larger outer parts of each flower 
# that protect the smaller inside petals before the flower buds bloom.

#EXERCISE
# load the iris dataset and use classification to see if the expected and predicted species match up
from sklearn.datasets import load_iris
iris = load_iris()

# display the shape of the data, target and target_names
print('\n')
print(iris.data.shape)
print(iris.target.shape)
print(iris.target_names)
print('\n')

# display the first 10 predicted and expected results using the species names not the number (using target_names)
# dictionary # dataframe

import pandas as pd
iris_df = pd.DataFrame(iris.target_names)
iris_df.reset_index(inplace=True)
iris_df.columns = ['Specie_Number','Specie_Name']
#print(iris_df)
print('\n')

from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(iris.data,iris.target, random_state=11)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X=data_train, y=target_train) 

predicted = knn.predict(X=data_test) 
predicted_df = pd.DataFrame(predicted)
predicted_df.columns = ['Specie_Number']
predicted_df = predicted_df.merge(iris_df,on='Specie_Number',how='left')
predicted_df = predicted_df.iloc[:,1] # remove specie_number column

expected = target_test
expected_df = pd.DataFrame(expected)
expected_df.columns = ['Specie_Number']
expected_df = expected_df.merge(iris_df,on='Specie_Number',how='left')
expected_df = expected_df.iloc[:,1] # remove specie_number column

print('First 10 Predicted Results:')
print('\n')
print(predicted_df[:10])
print('\n')
print('First 10 Expected Results:')
print('\n')
print(expected_df[:10])
print('\n')

# display the values that the model got wrong
wrong = [(p,e) for (p,e) in zip(predicted_df,expected_df) if p != e] # iterating through both lists at the same time
print('Values the Model Got Wrong:')
print(wrong)
print('\n')

# visualize the data using the confusion matrix
from sklearn.metrics import confusion_matrix
confusion = confusion_matrix(y_true=expected_df, y_pred=predicted_df) 
print('Confusion Matrix:')
print('\n')
print(confusion) 

# HEATMAP

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt2

confusion_df = pd.DataFrame(confusion, index=iris.target_names, columns=iris.target_names)
figure = plt2.figure(figsize=(7,6))
axes = sns.heatmap(confusion_df, annot=True, cmap=plt2.cm.nipy_spectral_r)
plt2.show() 