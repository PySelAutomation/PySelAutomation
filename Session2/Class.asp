# Define a class called 'Person'
class Person:
    # Constructor method to initialize object attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display information about the person
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create an instance of the 'Person' class
person1 = Person("Alice", 30)

# Access object attributes and call methods
person1.display_info()

# Create another instance of the 'Person' class
person2 = Person("Bob", 25)

# Access object attributes and call methods
person2.display_info()
