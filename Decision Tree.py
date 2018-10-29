from sklearn import tree

X=[[181,80,44],
   [177,70,43],
   [160,60,38],
   [154,54,37],
   [166,65,40],
   [190,90,47],
   [175,64,39],
   [171,75,42],
   [181,85,43]]

#Classification
Y=['male','female','female','female','male','male','male','female','female']

#Decision Tree Classifier
clf=tree.DecisionTreeClassifier()

#Trending Data
clf=clf.fit(X,Y)

#Predict
prediction=clf.predict([[190,70,43]])
print("Output = ",prediction)
