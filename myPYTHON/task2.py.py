class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am studying {self.course}.")

# Create three student objects
student1 = Student("Hayabusa", 23, "Aerospace Engineer")
student2 = Student("Lancelott", 22, "Architecture")
student3 = Student("Ling", 21, "Psychology")

# Call their introduce() method
student1.introduce()
student2.introduce()
student3.introduce()