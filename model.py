import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV, RepeatedStratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
import pickle




df = pd.read_csv("diabetes.csv")

df[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = df[['Glucose','BloodPressure','SkinThickness',
                                                                      'Insulin','BMI']].replace(0, np.NaN)
def median_target(var):   
    temp = df[df[var].notnull()]
    temp = temp[[var, 'Outcome']].groupby(['Outcome'])[[var]].median().reset_index()
    return temp

columns = df.columns
columns = columns.drop("Outcome")
for i in columns:
    median_target(i)
    df.loc[(df['Outcome'] == 0 ) & (df[i].isnull()), i] = median_target(i)[i][0]
    df.loc[(df['Outcome'] == 1 ) & (df[i].isnull()), i] = median_target(i)[i][1]

y = df["Outcome"]
X = df.drop(["Outcome"], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state = 2, stratify=y)

randomForest_params = {"n_estimators" : [100,500, 1000],
                       "min_samples_split" : np.arange(2,30),
                       "min_samples_leaf" : np.arange(1,50),
                       "max_features" : np.arange(1,7)}

random_forest = RandomForestClassifier()

cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=10, random_state=1)
random_search = RandomizedSearchCV(random_forest, randomForest_params, cv=cv, random_state=1, n_jobs=-1, verbose=2 )
pipe = make_pipeline(StandardScaler(),random_search)
pipe.fit(X_train, y_train)




pickle.dump(pipe, open("model.pkl","wb"))

model = pickle.load(open("model.pkl","rb"))






