import time

def countdown(t):
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end='\r')
    time.sleep(1)
    t-=1

  print("Fire at will!)

t = input("Enter the time in seconds: ")

# Validating user input
y = True
while y:
  try:
    t = int(t)
    y = False
  except:
    print("Must enter an integer to represent seconds\n")

# Running the countdown function
countdown(t)
