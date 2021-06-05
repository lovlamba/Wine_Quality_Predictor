import pandas as pd
import pickle

#Reading file and selecting features(x1) as well as the target value(y1)
df = pd.read_csv('wine.csv')
x1=df[['volatile acidity','alcohol','density','chlorides','type']].values
y1=df['goodq'].values

#Training the features and target value
from sklearn.tree import DecisionTreeClassifier
wineTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
wine = wineTree.fit(x1,y1)

#creating model.pkl
pickle.dump(wineTree,open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
