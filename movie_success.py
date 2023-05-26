
"""Original file is located at
    https://colab.research.google.com/drive/1txBiXoomiX9m-WUBPMZ_k7pd97BSs7Qb
"""
# edited here to generate GUI
import sklearn 
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv("movie_success_rate.csv")
df.head()
list(df.columns)

# Handling Missing Values

df.isnull().sum()
df.dropna(inplace=True)
df.head()

x = df[df.columns[7:32]]
y = df.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=99)

# Scaling the Data
scaler = StandardScaler()

print(y_train.shape, y_test.shape)

x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

# Random Forest

x_train = x_train.astype(int)
y_train = y_train.astype(int)
x_test = x_test.astype(int)
y_test = y_test.astype(int)


random_forest_model = RandomForestClassifier(n_estimators=60)
random_forest_model.fit(x_train, y_train)

y_predict = random_forest_model.predict(x_test)

confusion_matrix(y_test, y_predict)

accuracy = accuracy_score(y_predict, y_test)
