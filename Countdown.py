#import time
import time

timer = int(input("Enter time in seconds:"))

for x in reversed(range(1,timer + 1)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)
print("Time's up")
