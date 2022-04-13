from sklearn.datasets import load_digits

digits = load_digits() # bunch object # takes our entire dataset and put it into the digits object.
#print(digits.DESCR) # dataset characteristics

#print(digits.data[150]) # these sets of pixel intensities represent the number 0
#print(digits.target[150]) # The zero represent what the image is, so that's the target of these numbers.

print(digits.data[5]) # these sets of pixel intensities represent the number 5
print(digits.target[5]) # the first 9 images represent the first 9 classes, then it repeats over and over. because 1700 samples.

print(digits.data[:2]) # it's a numpy array # 0 to 16 because pixel intensity of each of these boxes
# the first sample has 64 features, we can't tell what the set of numbers represents.
print(digits.data.shape) # 8x8 # shape of the array, 1797 rows/samples and 64 columns/features

print(digits.target[:2]) # possible numbers: 0 to 9 because those are the target
print(digits.target.shape) # 1797 rows and only one column, the target is only one value, all these numbers point to number one. 
# the more samples we have, the more accurate the machine learning can learn.
# the more feature, the more looks at the different combinations of a number.
# target has 1797 rows, but 1 column, each of those rows represents a number, the target attribute is that number

print(digits.images[:2]) 
# the model needs a one dimensional array

import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))
for item in zip(axes.ravel(),digits.images,digits.target): # zip to iterate these objects at the same time # iterate together rather than seperately
    axes, image, target = item # see what the target is for that image
    axes.imshow(image,cmap=plt.cm.gray_r) # cmap = colormap
    axes.set_xticks([]) # remove tick marks for x and y axes / set empty/null
    axes.set_yticks([])
    axes.set_title(target) # title of each of those images is the target value
# ravel makes 2 dimensional into one dimension (1 row of 24 instead of 6x4)
plt.tight_layout()
#plt.show()

# MACHINE LEARNING
# split the data into into train and testing portions so that you can train your model with some data and test it to make sure it's working the way it should. 
# It produces 4 different lists/arrays
# Train your model with 75% of the data # randomly picks # we enter 11 to make sure all our codes match up.

from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(digits.data,digits.target, random_state=11)
print('lol')
print(data_train)
print(data_test)
print(data_train.shape) # 75% # 2D
print(data_test.shape)
print(target_train.shape) # 1D
print(target_test.shape)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X=data_train, y=target_train) # x upper case is the sample and y lower case is the target
# fit is the method that is doing ALL THE MACHINE MEARNING needs the data and the target to know what that data represents
# each row has a target, it's going to look at those numbers and look for the target value 
# as long as you tell it what the target is, it's going to learn.
# tell it what the target is so it can learn
# input = all the samples with all the features, the mroe features/samples you have, the better it's going to predict
# y = the target value

predicted = knn.predict(X=data_test) # give some unlabeled data and see if it can guess what that number is 
# no y because it's supposed to spit out the answer
expected = target_test
# how do we know if the answer is correct or not? We compare it to what it's supposed to be, the target_test
# expected and # predicted should match up
# it's going to produce the results/LIST that it thinks it's supposed to be

print(predicted[:20])
print(expected[:20])

# see how well it predicted it
print(format(knn.score(data_test,target_test),".2%"))

# see which ones it got wrong
wrong = [(p,e) for (p,e) in zip(predicted,expected) if p != e] # iterating through both lists at the same time
print(wrong) # got 10 wrong out of 450

# how can we improve the model
# Confusion Matrix to see what and how far it got wrong
from sklearn.metrics import confusion_matrix
confusion = confusion_matrix(y_true=expected, y_pred=predicted) 
print(confusion) # 10 rows and 10 columns
# 1st row = 1st class = number 0, it hasn't messed up
# for number 3, it messed up twice, it was supposed to guess 3, but it guessed 5 and 7

# easier to create a heatmap

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt2

confusion_df = pd.DataFrame(confusion, index=range(10), columns=range(10))
figure = plt2.figure(figsize=(7,6))
axes = sns.heatmap(confusion_df, annot=True, cmap=plt2.cm.nipy_spectral_r)
plt2.show() # the higher the number, the darkest the color
# solution: to add more samples
