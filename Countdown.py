#import time
import time

timer = int(input("Enter time in seconds:"))

for x in reversed(range(1,timer + 1)):
    print(x)
    time.sleep(1)

   

print("Time's up")
