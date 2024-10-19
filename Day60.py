# Getters and Setters in python


class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    # This function work like a getter
    @property
    def ten_value(self):
        return 10 * self._value

    # This function work like a setter
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10


# Set Class value here
obj = MyClass(10)

# Change value for setter
obj.ten_value = 67

# Print getter value
print(obj.ten_value)

# Call show function here for print class, getter, setter value
obj.show()
