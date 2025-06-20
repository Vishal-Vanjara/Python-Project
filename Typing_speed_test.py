from re import error
from time import *
import random as r


def mistake(paratest, usertest):
  error = 0
  for i in range(len(paratest)):
    try:
      if paratest[i] != usertest[i]:
        error = error + 1
    except:
      error = error + 1
  return error


def speed_time(time_start, time_end, userinput):
  time_delay = time_end - time_start
  time_R = round(time_delay, 2)
  speed = len(userinput) / time_R
  return round(speed)


test = [
    "This pleasantly unique film is not just a love story",
    "it is a life story",
    "It showcases a variety of relationships that go beyond the traditional."
]

test1 = r.choice(test)
print("^^^^^^^^^^^Typing Test^^^^^^^^^^^^^^^^")
print(test1)
print()
print()
time_1 = time()
testinput = input("Enter :")
time_2 = time()

print("Speed :", speed_time(time_1, time_2, testinput), "w/sec")
print("Error", mistake(test1, testinput))
