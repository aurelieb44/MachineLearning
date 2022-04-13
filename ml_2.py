import pandas as pd
from sklearn.model_selection import train_test_split

nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')
print(nyc.head(3))
# temperature is the target # date is our data
# each column of a dataframe is a series 
# we have to separate the date from the target

print(nyc.Date.values) # one dimensional but format is incorrect
# expects to be in two dimensions, needs rows because it has to be a sample
# need to reshape it

print(nyc.Date.values.reshape(-1,1))
# -1 = number of rows # it automatically infers it based on the data because we don't know how many rows there are
# 1 = number of columns
# only want one column
# we know it's two-dimensional because two brackets, bunch of rows and only one column

X_train, X_test, y_train, y_test = train_test_split(nyc.Date.values.reshape(-1,1), nyc.Temperature.values, random_state = 11)
# first argument: the data/sample
# second argument
# random_state = if we don't do it, it may be split differently for different people
print('lovr')
print(X_train)
print(X_test)
print(X_train.shape)
print(X_test.shape)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X=X_train, y=y_train) # where learning takes place

print(lr.coef_)
print(lr.intercept_)

predicted = lr.predict(X_test) # no y because the purpose is to produce the result
expected = y_test

for p,e in zip(predicted[::5], expected[::5]): # check every 5 element
    print(f'predicted: {p:.2f}, expected {e:.2f}')

predict = (lambda x: lr.coef_ * x + lr.intercept_)
print(predict(2025))
print(predict(1890))

import seaborn as sns
axes = sns.scatterplot(
    data=nyc,
    x='Date',
    y='Temperature',
    hue='Temperature',
    palette='winter',
    legend=False)

axes.set_ylim(10,70)
import numpy as np
x = np.array([min(nyc.Date.values),max(nyc.Date.values)])
print(x)
y = predict(x)
print(y)

import matplotlib.pyplot as plt
line = plt.plot(x,y)
plt.show()