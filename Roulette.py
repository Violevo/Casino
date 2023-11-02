import random

money = 100
int(money)

red = (1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36)
black = (2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35)
even = (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36)
odd = (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35)
n1to18 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
n19to36 = (19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)
n1st12 = (1,2,3,4,5,6,7,8,9,10,11,12)
n2nd12 = (13,14,15,16,17,18,19,20,21,22,23,24)
n3rd12 = (25,26,27,28,29,30,31,32,33,34,35,36)

def bet():
    num = int(input("how much to bet?"))
    print  ("you have money:", money)
    money = money - num
    place = input ("what to bet on? (red,black,even,odd,1to18,19to36,1st12,2nd12,3rd12)")

num = int(input("how much to bet?"))
money = money - num
place = input ("what to bet on? (red,black,even,odd,1to18,19to36,1st12,2nd12,3rd12)")

while 1:
    go = input("would you like to bet again?")
    if go == "yes":
        bet()
    else:
        break

spin = random.randint (0,36)


if place == "red":
    if red == spin:
        print ("you Won")
        money = money + num * 2
        print ("you have money",money)
    else:
        print ("HAHA YOU LOOSE")
    
