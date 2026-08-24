import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import os
dataset_path = "dataset.csv"
if not os.path.exists(dataset_path):
    dataset_path = "Day-04-Machine-Learning/Regression/dataset.csv"
df = pd.read_csv(dataset_path)

x = df[["StudyHours","Attendance"]]
y=df["Score"]

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(x_train,y_train)

print("Model training completed")

from sklearn.metrics import mean_absolute_error, mean_squared_error

prediction=model.predict(x_test)
print(prediction)

accuracy=mean_absolute_error(y_test,prediction)
accuracy1=mean_squared_error(y_test,prediction)
print("mae:",accuracy)
print("mse:",accuracy1)


new_student = pd.DataFrame([[3,85]], columns=["StudyHours", "Attendance"])
predicted_Score = model.predict(new_student)
print("Predicted score:", predicted_Score)
