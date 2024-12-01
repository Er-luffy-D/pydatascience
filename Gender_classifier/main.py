from sklearn import tree


# O-for Male , 1-Female
class_dict={0:"Male",1:"Female"}

# Data created by ChatGPT
# [height,width,shoe size]
X = [
    [175, 70, 42],  # Male
    [160, 55, 38],  # Female
    [180, 80, 44],  # Male
    [165, 60, 39],  # Female
    [170, 68, 41],  # Male
    [158, 54, 37],  # Female
    [185, 90, 45],  # Male
    [162, 58, 38],  # Female
    [172, 72, 42],  # Male
    [155, 50, 36],  # Female
    [178, 75, 43],  # Male
    [167, 62, 39],  # Female
    [182, 85, 44],  # Male
    [159, 53, 37],  # Female
    [174, 73, 42],  # Male
    [164, 57, 38],  # Female
]
Y = [
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
]

# Using decision tree classifier
clf= tree.DecisionTreeClassifier()
# training the tree on X and Y
clf=clf.fit(X,Y)
# predicting
prediction=clf.predict([[175,59,42]])
print(class_dict[prediction.item()])