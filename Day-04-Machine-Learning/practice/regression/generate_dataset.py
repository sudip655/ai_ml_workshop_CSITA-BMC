import pandas as pd

data = {
    "StudyHours": [
        2.5, 3.0, 4.5, 5.0, 6.0, 1.5, 2.0, 3.5, 4.0, 5.5,
        6.5, 7.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.5, 1.0, 2.0
    ],
    "Attendance": [
        75, 80, 85, 90, 88, 70, 72, 78, 82, 90,
        95, 92, 68, 76, 84, 86, 93, 96, 65, 70
    ],
    "Score": [
        45, 50, 65, 72, 75, 38, 42, 55, 60, 78,
        85, 88, 40, 48, 62, 70, 82, 92, 30, 40
    ]
}

df = pd.DataFrame(data)

df.to_csv("Day-04-Machine-Learning/Regression/dataset.csv", index=False)

print("Dataset generated and saved to Day-04-Machine-Learning/Regression/dataset.csv")
print(df.head())
