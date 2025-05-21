from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_number: int
    grade: str

# Creating a student object
student1 = Student(name="Ahmed", roll_number=101, grade="A")

# Printing student details
print(student1)


from typing import TypeVar, Generic

T = TypeVar('T')  # T koi bhi type ho sakta hai

class StorageBox(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def get_item(self) -> T:
        return self.item

# Creating boxes for different types of items
pen_box = StorageBox("Blue Pen")
number_box = StorageBox(100)
tools_box = StorageBox(["Hammer", "Wrench", "Screwdriver"])

print("Pen:", pen_box.get_item())
print("Number:", number_box.get_item())
print("Tools:", tools_box.get_item())
