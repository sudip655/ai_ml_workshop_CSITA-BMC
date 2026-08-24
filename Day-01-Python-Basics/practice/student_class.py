# Practice Task 5: Create a Student class with marks and grade method.

class Student:
    def __init__(self, name, marks):
        """
        Initialize Student object.
        name: str
        marks: dict or list of numeric grades
        """
        self.name = name
        self.marks = list(marks) if isinstance(marks, (list, tuple)) else list(marks.values())

    def get_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        average = self.get_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def introduce(self):
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Grade: {self.get_grade()}")

def main():
    print("=== Student Record System ===")
    
    # Create sample students
    s1 = Student("Sudeep", [85, 92, 78, 90])
    s2 = Student("Amit", [58, 62, 70, 65])
    s3 = Student("Rakshya", [95, 98, 96, 94])
    
    for s in [s1, s2, s3]:
        s.introduce()
        print("-" * 30)

if __name__ == "__main__":
    main()
