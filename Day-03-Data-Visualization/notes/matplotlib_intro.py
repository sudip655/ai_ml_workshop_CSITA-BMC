# =========================================================
# DAY 3 - PART 1: Introduction to Data Visualization (Matplotlib)
# -----------------------------------------------------------
# What this file does:
#   - Shows how to create standard line plots, bar charts, and scatter plots.
#   - Demonstrates customizing styles: colors, markers, grid, titles, and legends.
#   - Uses non-blocking showing so they can run easily.
# =========================================================

import matplotlib.pyplot as plt
import numpy as np

def run_line_plot():
    print("Generating line plot...")
    # Sample data
    days = np.arange(1, 8)
    temperatures = np.array([22, 24, 21, 23, 25, 28, 27])

    plt.figure(figsize=(8, 4))
    plt.plot(days, temperatures, marker='o', color='purple', linestyle='--', linewidth=2, label="Temp (°C)")
    plt.title("Weekly Temperature Trends", fontsize=14, fontweight='bold')
    plt.xlabel("Day of Week")
    plt.ylabel("Temperature (°C)")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.show()

def run_bar_chart():
    print("Generating bar chart...")
    # Sample data
    subjects = ["Python", "NumPy", "Pandas", "ML"]
    average_scores = [78.5, 82.1, 79.8, 85.4]

    plt.figure(figsize=(8, 4))
    plt.bar(subjects, average_scores, color=['#4285F4', '#34A853', '#FBBC05', '#EA4335'], edgecolor='black', alpha=0.85)
    plt.title("Average Marks by Subject", fontsize=14, fontweight='bold')
    plt.xlabel("Subjects")
    plt.ylabel("Average Score")
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def run_scatter_plot():
    print("Generating scatter plot...")
    # Sample data: study hours vs exam scores
    study_hours = np.array([2.5, 5.0, 3.2, 8.5, 7.0, 1.5, 9.0, 6.0])
    exam_scores = np.array([45, 72, 58, 88, 80, 38, 95, 75])

    plt.figure(figsize=(8, 4))
    plt.scatter(study_hours, exam_scores, color='red', marker='x', s=100, label="Students")
    plt.title("Study Hours vs. Exam Score", fontsize=14, fontweight='bold')
    plt.xlabel("Hours Studied")
    plt.ylabel("Exam Score")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    print("=== Matplotlib Visualization Demo ===")
    run_line_plot()
    run_bar_chart()
    run_scatter_plot()

if __name__ == "__main__":
    main()
