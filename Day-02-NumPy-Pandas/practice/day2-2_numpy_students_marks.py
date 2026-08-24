import numpy as np


students = np.array(
    [
        "Ram",
        "Sita",
        "Hari",
        "Gita",
        "Asha",
        "Bikash",
        "Nisha",
        "Kiran",
        "Anil",
        "Sabina",
        "Ramesh",
        "Puja",
    ]
)

marks = np.array(
    [
        [78, 85, 82, 88],
        [65, 72, 70, 68],
        [90, 92, 95, 94],
        [55, 60, 58, 62],
        [72, 75, 78, 80],
        [88, 84, 86, 90],
        [60, 65, 62, 64],
        [95, 96, 94, 98],
        [70, 68, 72, 75],
        [82, 80, 85, 87],
        [58, 62, 65, 60],
        [86, 89, 91, 93],
    ]
)

subjects = np.array(["Python", "NumPy", "Statistics", "Machine Learning"])

num_students, num_subjects = marks.shape
print(
    f"1. Total Students: {num_students} | Total Subjects: {num_subjects}\n"
)


print("2. Complete Marks Table:")
print(f"{'Student':<10} | " + " | ".join([f"{sub:>16}" for sub in subjects]))
print("-" * 80)
for name, row in zip(students, marks):
    print(f"{name:<10} | " + " | ".join([f"{m:>16}" for m in row]))
print("\n" + "=" * 80 + "\n")

student_totals = marks.sum(axis=1)
student_averages = marks.mean(axis=1)
student_max = marks.max(axis=1)
student_min = marks.min(axis=1)

highest_avg_idx = np.argmax(student_averages)
print(
    f"7. Highest Average: {students[highest_avg_idx]} ({student_averages[highest_avg_idx]:.2f})"
)

lowest_avg_idx = np.argmin(student_averages)
print(
    f"8. Lowest Average : {students[lowest_avg_idx]} ({student_averages[lowest_avg_idx]:.2f})\n"
)

subject_averages = marks.mean(axis=0)
for sub, avg in zip(subjects, subject_averages):
    print(f"9. Average for {sub}: {avg:.2f}")
print()

subject_max = marks.max(axis=0)
for sub, mx in zip(subjects, subject_max):
    print(f"10. Highest mark in {sub}: {mx}")
print()

ml_index = np.where(subjects == "Machine Learning")[0][0]
top_ml_student_idx = np.argmax(marks[:, ml_index])
print(
    f"11. Top Scorer in Machine Learning: {students[top_ml_student_idx]} ({marks[top_ml_student_idx, ml_index]})\n"
)

high_achievers = students[student_averages >= 80]
print(f"12. Students with Average >= 80: {', '.join(high_achievers)}")

below_60_mask = np.any(marks < 60, axis=1)
students_below_60 = students[below_60_mask]
print(
    f"13. Students scoring < 60 in at least one subject: {', '.join(students_below_60)}\n"
)

subject_std = marks.std(axis=0)
for sub, std in zip(subjects, subject_std):
    print(f"14. Std Dev for {sub}: {std:.2f}")
print()

# 15. Assign grades
conditions = [
    student_averages >= 85,
    student_averages >= 70,
    student_averages >= 60,
]
choices = ["A", "B", "C"]
grades = np.select(conditions, choices, default="D")

percentages = (student_totals / (num_subjects * 100)) * 100

ranked_indices = np.argsort(student_averages)[::-1]
ranks = np.empty_like(ranked_indices)
ranks[ranked_indices] = np.arange(1, num_students + 1)

min_val = marks.min()
max_val = marks.max()
normalized_marks = (marks - min_val) / (max_val - min_val)


print("\n" + "=" * 80)
print("19. FINAL STUDENT PERFORMANCE REPORT")
print("=" * 80)
print(
    f"{'Rank':<5} | {'Student':<10} | {'Total':<6} | {'Avg':<6} | {'Max':<4} | {'Min':<4} | {'Pct':<6} | {'Grade':<5}"
)
print("-" * 80)


for idx in ranked_indices:
    print(
        f"{ranks[idx]:<5} | "
        f"{students[idx]:<10} | "
        f"{student_totals[idx]:<6} | "
        f"{student_averages[idx]:<6.2f} | "
        f"{student_max[idx]:<4} | "
        f"{student_min[idx]:<4} | "
        f"{percentages[idx]:<6.2f}% | "
        f"{grades[idx]:<5}"
    )

print("=" * 80)
