''' Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line '''

import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

#how many samples and How many features?
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
print(diabetes.data.shape) # 442 samples and 10 features
#print(diabetes.data[:6])

# What does feature s6 represent?
print(diabetes.DESCR) # glu, blood sugar level

#print out the coefficient
#print out the intercept
from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(diabetes.data, diabetes.target, random_state = 11)
print(data_train)
print(data_test)
print(data_train.shape) 
print(data_test.shape)
#print(target_train.shape) 
#print(target_test.shape)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X=data_train, y=target_train) # where learning takes place

print('coefficient: ', lr.coef_)
print('intercept: ', lr.intercept_)

# create a scatterplot with regression line

predicted = lr.predict(data_test) 
expected = target_test
plt.plot(expected,predicted, '.')
x = np.linspace(0,330,100)
y = x

plt.plot(x,y)
plt.show()