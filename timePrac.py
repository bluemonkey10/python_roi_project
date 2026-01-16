import time
import keyboard

def countdown(t):
  while t:
    mins, secs = divmod(t, 60)
    timer = f"{mins:02d}:{secs:02d}"
    print(timer, end='\r')
    time.sleep(1)
    t-=1

  print("Fire at will!")

def stopwatch():
  while True:
    print(keyboard.read_key())
    if keyboard.read_key() == "a":
      break

# Validating user input
y = True
while y:
  try:
    t = input("Enter the time in seconds: ")
    t = int(t)
    y = False
  except:
    print("Must enter an integer to represent seconds\n")

# Running the countdown function
countdown(t)
stopwatch()
