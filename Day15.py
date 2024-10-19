# Exercise 2

import time

timestamp = int(time.strftime("%H"))

if timestamp >= 0 and timestamp < 12:
    print("Good Morning")
elif timestamp > 12 and timestamp <= 18:
    print("Good Afternoon")
# elif timestamp > 18 and timestamp < 24:
#     print("Good Evening")

else:
    print("Good Evening")