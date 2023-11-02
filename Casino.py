from pathlib import Path
import pathlib
import os
import glob
path = Path(__file__).parents[0]
print (path)
os.chdir(path)
game = input("what game do you  want to play (Slots,Roulette,Blackjack): ")
if game == ("Slots"):
    os.system("Slots.py")
    print ("Slots Window Opened")
if game == ("Roulette"):
    os.system("Roulette.py")
    print ("Roulette Window Opened")
