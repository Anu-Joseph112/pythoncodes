class Time:
    def __init__(self, hours, minutes):
        self.__hours = hours
        self.__minutes = minutes

    def __add__(self, other):
        total_minutes = self.__minutes + other.__minutes
        total_hours = self.__hours + other.__hours

        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60

        return Time(total_hours, total_minutes)

    def display(self):
        print(self.__hours, "Hours", self.__minutes, "Minutes")


# Creating two time objects
t1 = Time(2, 45)
t2 = Time(3, 30)

print("First Time:")
t1.display()

print("Second Time:")
t2.display()

# Adding two times
t3 = t1 + t2

print("Sum of Two Times:")
t3.display()
