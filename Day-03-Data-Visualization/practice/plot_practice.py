# Practice Task: Create visual charts representing student marks and performance.

import matplotlib.pyplot as plt
import numpy as np

# Sample data representing students, their average marks, and study hours
students = ["Ram", "Sita", "Hari", "Gita", "Asha", "Bikash", "Nisha", "Kiran", "Anil", "Sabina", "Ramesh", "Puja"]
averages = [83.25, 68.75, 92.75, 58.75, 76.25, 87.00, 62.75, 95.75, 71.25, 83.50, 61.25, 89.75]
study_hours = [8, 6, 10, 4, 7, 9, 5, 11, 6, 8, 3, 10]

def main():
    print("=== Student Performance Visualizer ===")
    
    # Create a figure with two subplots side-by-side or stacked
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar chart for Averages on primary y-axis
    color = 'teal'
    ax1.set_xlabel('Students', fontweight='bold')
    ax1.set_ylabel('Average Marks', color=color, fontweight='bold')
    bars = ax1.bar(students, averages, color=color, alpha=0.6, label='Average Marks', edgecolor='black')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 100)
    plt.xticks(rotation=45)

    # Line plot for Study Hours on secondary y-axis
    ax2 = ax1.twinx()  
    color = 'crimson'
    ax2.set_ylabel('Study Hours (Weekly)', color=color, fontweight='bold')
    line = ax2.plot(students, study_hours, color=color, marker='o', linewidth=2, label='Study Hours')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, 12)

    plt.title('Student Average Marks vs Weekly Study Hours', fontsize=14, fontweight='bold')
    fig.tight_layout()  # Adjust layout to make room for x-labels
    
    print("Displaying student comparison plot...")
    plt.show()

if __name__ == "__main__":
    main()
