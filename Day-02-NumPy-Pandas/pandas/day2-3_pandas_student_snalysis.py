import pandas as pd
import numpy as np

data = {
    "student_id": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112
    ],
    "name": [
        "Ram", "Sita", "Hari", "Gita",
        "Asha", "Bikash", "Nisha", "Kiran",
        "Anil", "Sabina", "Ramesh", "Puja"
    ],
    "age": [
        21, 22, 20, 23,
        21, 24, 22, 20,
        23, 21, 25, 22
    ],
    "gender": [
        "M", "F", "M", "F",
        "F", "M", "F", "M",
        "M", "F", "M", "F"
    ],
    "python": [
        78, 65, 90, 55,
        72, 88, 60, 95,
        70, 82, 58, 86
    ],
    "numpy": [
        85, 72, 92, 60,
        75, 84, 65, 96,
        68, 80, 62, 89
    ],
    "pandas": [
        82, 70, 95, 58,
        78, 86, 62, 94,
        72, 85, 65, 91
    ],
    "machine_learning": [
        88, 68, 94, 62,
        80, 90, 64, 98,
        75, 87, 60, 93
    ],
    "attendance": [
        92, 85, 96, 70,
        88, 94, 75, 98,
        82, 91, 68, 95
    ],
    "study_hours": [
        8, 6, 10, 4,
        7, 9, 5, 11,
        6, 8, 3, 10
    ]
}
df = pd.DataFrame(data)

subject_cols = ["python", "numpy", "pandas", "machine_learning"]

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)


def section(title):
    print("\n" + "=" * 90)
    print(title)
    print("=" * 90)



section("1. First 5 rows")
print(df.head())

section("2. Last 5 rows")
print(df.tail())

section("3. Shape")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

section("4. Column names")
print(list(df.columns))

section("5. Data types")
print(df.dtypes)

section("6. Statistical summary (describe)")
print(df.describe())



df["total_marks"] = df[subject_cols].sum(axis=1)
df["average_marks"] = df[subject_cols].mean(axis=1)
df["percentage"] = (df["total_marks"] / (len(subject_cols) * 100)) * 100

section("7. Total marks per student")
print(df[["name", "total_marks"]])

section("8. Average marks per student")
print(df[["name", "average_marks"]].round(2))

section("9. Percentage per student")
print(df[["name", "percentage"]].round(2))

top_student = df.loc[df["average_marks"].idxmax()]
section("10. Highest-performing student")
print(f"{top_student['name']} — Average: {top_student['average_marks']:.2f}")

bottom_student = df.loc[df["average_marks"].idxmin()]
section("11. Lowest-performing student")
print(f"{bottom_student['name']} — Average: {bottom_student['average_marks']:.2f}")

section("12. Highest mark in each subject")
print(df[subject_cols].max())

section("13. Average for each subject")
print(df[subject_cols].mean().round(2))



section("14. Students with average > 80")
print(df.loc[df["average_marks"] > 80, ["name", "average_marks"]])

section("15. Students with attendance < 75%")
print(df.loc[df["attendance"] < 75, ["name", "attendance"]])

section("16. Students who studied more than 8 hours")
print(df.loc[df["study_hours"] > 8, ["name", "study_hours"]])

section("17. Students who scored above 80 in Machine Learning")
print(df.loc[df["machine_learning"] > 80, ["name", "machine_learning"]])

below_60_mask = (df[subject_cols] < 60).any(axis=1)
section("18. Students who scored below 60 in at least one subject")
print(df.loc[below_60_mask, ["name"] + subject_cols])


section("19. Average marks by gender (per subject)")
print(df.groupby("gender")[subject_cols].mean().round(2))

section("20. Average attendance by gender")
print(df.groupby("gender")["attendance"].mean().round(2))

section("21. Average study hours by gender")
print(df.groupby("gender")["study_hours"].mean().round(2))



df["rank"] = df["average_marks"].rank(ascending=False, method="min").astype(int)
df_ranked = df.sort_values("rank")

section("22. Students ranked by average marks")
print(df_ranked[["rank", "name", "average_marks"]].round(2))

section("23. Top 5 students")
print(df_ranked[["rank", "name", "average_marks"]].head(5).round(2))



section("24. Correlation between study hours and marks")
corr_with_study = df[["study_hours"] + subject_cols].corr()["study_hours"].drop("study_hours")
print(corr_with_study.round(3))

ml_corr = df["study_hours"].corr(df["machine_learning"])
section("25. Correlation: study hours vs Machine Learning marks")
if ml_corr >= 0.7:
    strength = "a strong positive"
elif ml_corr >= 0.4:
    strength = "a moderate positive"
elif ml_corr >= 0:
    strength = "a weak positive"
else:
    strength = "a negative"
print(f"Correlation coefficient: {ml_corr:.3f} -> {strength} correlation")


def performance_label(avg):
    if avg >= 85:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    elif avg >= 60:
        return "Average"
    else:
        return "Poor"


df["performance"] = df["average_marks"].apply(performance_label)
df_ranked = df.sort_values("rank")  

section("26. Performance category per student")
print(df[["name", "average_marks", "performance"]].round(2))



section("FINAL STUDENT PERFORMANCE REPORT")
final_report = df_ranked[
    ["rank", "student_id", "name", "gender", "total_marks",
     "average_marks", "percentage", "attendance", "study_hours", "performance"]
].round(2)
print(final_report.to_string(index=False))
