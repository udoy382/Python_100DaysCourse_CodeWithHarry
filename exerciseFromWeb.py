# Exercise 1
"""
list1 = [100, 200, 300, 400, 500]

# list1.reverse()
# print(list1)

new_list = list1[::-1]
print(new_list)
"""

# Exercise 2
"""
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

output = [i + j for i,  j in zip(list1, list2)]
print(output)
"""

# Exercise 3
"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

output = [i + j for i in list1 for j in list2]
print(output)
"""

# Exercise 4

"""
def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
    
result1 = multiplication_or_sum(20, 30)
print(result1)

result2 = multiplication_or_sum(40, 30)
print(result2)
"""

# Exercise 5

"""
previous_number = 0

for i in range(1,10):
    x_sum = previous_number + i
    print("current number ", i, "previous number ", previous_number, "some of number is ", x_sum)

    previous_number = i
"""

# Exercise 6

"""
name = input("Enter you name: ")
age = int(input("Enter your age: "))

year = 2005 - age + 60

print("Hi " + name, "your age will be 100 in", year, " year")
"""