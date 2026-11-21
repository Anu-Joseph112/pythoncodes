class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

    def __lt__(self, other):
        return self.area() < other.area()


# Creating two rectangle objects
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)
print("area or r1",r1.area())
print("area or r2",r2.area())

# Comparing areas
if r1 < r2:
    print("Area of first rectangle is smaller")
elif r2 < r1:
    print("Area of second rectangle is smaller")
else:
    print("Both have same area")
