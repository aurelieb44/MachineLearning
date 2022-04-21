# Classes.csv  - is a file describing the class an animal belongs to as well as the name of the class. 
# The class number and class type are the two values that are of most importance to you.

# animals_train.csv - is the file you will use to train your model. 
# There are 101 samples with 17 features. The last feature is the class number 
# (corresponds to the class number from the classes file). 
# This should be used as your target attribute. 
# However, we want the target attribute to be the class type (Mammal, Bird, Reptile, etc.) instead of the class number (1,2,3,etc.).

# animals_test.csv - is the file you will use to test your model to see if it can correctly predict the class that each sample belongs to. 
# The first column in this file has the name of the animal (which is not in the training file).  
# Also, this file does not have a target attribute since the model should predict the target class.

# GET THE DATA

import pandas as pd

data_test_og = pd.read_csv('animals_test.csv')
data_test = data_test_og.iloc[:,1:] # remove animal name/first column
#data_test = data_test_og.loc[:,['animal_name']]
print('\n')
print(data_test[:10])
data_train_og = pd.read_csv('animals_train.csv')
data_train = data_train_og.iloc[:,:16] # remove class number/last column
print('\n')
print(data_train[:10])

#target_train = data_train_og[['class_number']]
target_train = data_train_og.iloc[:,16] # only keep class number/last column
#target_train = data_train_og.loc[:,['class_number']]
print('\n')
print(target_train[:10])

animals = pd.read_csv('animal_classes.csv')
animals = animals.loc[:,['Class_Number','Class_Type']] # only keep class number and class type / find matches
print('\n')
print(animals)

# MACHINE LEARNING

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X=data_train, y=target_train)

# PREDICTIONS

predicted = knn.predict(X=data_test)
print('\n')
print(predicted)

# DATA FRAME

predicted_df = pd.DataFrame(predicted)
predicted_df.columns = ['Class_Number'] # dataframe with class number/prediction

predicted_df = pd.merge(predicted_df,data_test_og['animal_name'],left_index=True, right_index=True) # add animal_name column
predicted_df = predicted_df.merge(animals,on='Class_Number',how='left') # add class_type column based on class

predicted_df = predicted_df.iloc[:,1:] # remove class_number
predicted_df.columns = ['animal_name','prediction'] # rename columns
print('\n')
print(predicted_df)

# CSV FILE

predicted_df.to_csv('QuizII_Predictions.csv', sep=',', index=False)


