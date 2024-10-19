# Multithreading in Python


import threading
import time

# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# Normal code
time1 = time.perf_counter()
# func(4)
# func(2)
# func(1)
# time2 = time.perf_counter()
# print(time2 - time1)


# Same code using Thread
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

# t1.join()
# t2.join()
# t3.join()

# Calculating time 
time2 = time.perf_counter()
print(time2 - time1)