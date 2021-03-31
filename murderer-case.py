import random
from time import sleep
import os
start = input("Pres ENTER to start the game. "
if start == "":
  os.system("clear")
  print("Loading...")
  sleep(5)
  os.system("clear")
  print("Scanning Island...")
  sleep(5)
  os.system("clear")
  land =- input("Welcoime to the Flight Mobile! Press ENTER to land. "
  if land == "":
    os.system("clear")
    print("Your are skydiving")
    parachute = input("Press ENTER to open your parachute. "
    if parachute == "":
      os.system("clear")
      print("You have deployed your parachute. You are going to land in 5 seconds.")
      sleep(5)
      os.system("clear")
      print("You have landed.")
      sleep(2)
      numbers = "1","2","3","4","5","6","7","8","9","0"
      x = random.randint(0,9)
      y = random.randint(0,9)
      x1 = 0
      y1 = 0
      mc = x,y
      pc = x1,y1
      print("You are on the coordinate of",x1,",",y1)
      print("There is a murderer on the loose. You have to catch him. When you receive the message that you are near him, type kill and you will win this game.")
      for i in range(10):
        if pc == mc:
          os.system("clear")
          kill = input("You are near the killer, type kill now  ")
          if kill == "kill":
           print("Mission 1 was a success.")
        move = input("If you press 8 you go 1 step forword. If you press 2 you go 1 step back. If you press 4 you go 1 step left and if you press 6 you go 1 step right.")
