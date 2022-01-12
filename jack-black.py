#author Tanner Mesaric
import random
def deal():
    rCard = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    num = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    for i in range(len(rCard)):
        ranNum = random.choice(num)
        if ranNum == "0":
            print("Ace")
            return 1
        elif ranNum == "1":
            print("2")
            return 2
        elif ranNum == "2":
            print("3")
            return 3
        elif ranNum == "3":
            print("4")
            return 4
        elif ranNum == "4":
            print("5")
            return 5
        elif ranNum == "5":
            print("6")
            return 6
        elif ranNum == "6":
            print("7")
            return 7
        elif ranNum =="7":
            print("8")
            return 8
        elif ranNum =="8":
            print("9")
            return 9
        elif ranNum =="9":
            print("10")
            return 10
        elif ranNum=="10":
            print("jack")
            return 10
        elif ranNum=="11":
            print("queen")
            return 10
        elif ranNum=="12":
            print("King")
            return 10

def player_extra_deal(playersHand):
    
    print("*****Your Turn*****")
    
    while True:
        if playersHand < 21:
            dorNo = input("Do you want another card? (Y)es or (N)o: ").lower().strip()
            if dorNo =="y":
                playersHand += deal()
                print(f"Your total: {playersHand}")
            elif dorNo =="n" or playersHand >= 21:
                return playersHand
        elif playersHand >= 21:
            return playersHand 
    return playersHand 

def computer_extra_deal(computersHand):
    print("*****Computers Turn:*****")
    while True:
        if computersHand < 14:
            computersHand += deal()
        elif computersHand > 14:
            print("Computer does not deal")
            return computersHand
    return computersHand





print("Welcome to the Game of 21!")
print(f"""
***** Your Hand: *****""")
playersHand = deal() + deal()
print(f"Your Total: {playersHand}")
print(f"""
***** Computers Hand: *****""")
computersHand = deal() + deal()
print(f"""Computers total: {computersHand}
""")


yTurn = player_extra_deal(playersHand)


cTurn = computer_extra_deal(computersHand)
print(f"""
Computers total {cTurn}
""")

print("***** Game Over: *****")
if yTurn > 21:
    print("You loose")
if cTurn > 21:
    print("computer looses")
if yTurn == cTurn:
    print("Tie")
if yTurn > cTurn and yTurn <= 21:
    print("YOU WON")
if cTurn > yTurn and cTurn <= 21:
    print("YOU SUCK")