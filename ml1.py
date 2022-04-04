from sklearn.datasets import load_digits

digits = load_digits()

print(digits.data[:2]) # it's a numpy array # 0 to 16 because pixel intensity of each of these boxes
# the first sample has 64 features, we can't tell what the set of numbers represents.
print(digits.data.shape) # 8x8 # shape of the array, 1797 rows and 64 columns

print(digits.target[:2]) # possible numbers: 0 to 9 because those are the target
print(digits.target.shape) # 1797 rows and only one column, the target is only one value, all these numbers point to number one. 
# the more samples we have, the more accurate the machine learning can learn.
# the more feature, the more looks at the different combinations of a number.

print(digits.images[:2]) 
# the model needs a one dimensional array

import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))
for item in zip(axes.ravel(),digits.images,digits.target): # zip to iterate these objects at the same time # iterate together rather than seperately
    axes, image, target = item # see what the target is for that image
    axes.imshow(image,cmap=plt.cm.gray_r)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)

plt.tight_layout()
plt.show()
