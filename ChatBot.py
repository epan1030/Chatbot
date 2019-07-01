
# --- Define your functions below! ---
from random import *
def intro():
    print("Hey I'm Chatbot 3000! I am here to entertain ya!")
def say_hello(name):
    print("Hi" + name)

def menugenerator():
    aListMainCourse = ["Hamburger", "Pizza", "Pasta", "Salad"]
    bListSides = ["Fries", "Onion Rings", "Mashed Potatoes", "Bread Slices"]
    aRandomIndex = randint(0, len(aListMainCourse)-1)
    bRandomIndex = randint(0, len(bListSides)-1)
    print(aListMainCourse[aRandomIndex])
    print(bListSides[aRandomIndex])

def haikugenerator():
        aListFiveSyllable = ["You are amazing", "I love you so much", "You are beautiful"]
        aListSevenSyllable = ["You are the moon to my stars", "Your caring heart makes my day"]
        aListFiveSyllable2 = ["Thanks for being you", "You are loved dearly"]
        aRandomIndex = randint(0, len(aListFiveSyllable)-1)
        aRandomIndex = randint(0, len(aListSevenSyllable)-1)
        aRandomIndex = randint(0, len(aListFiveSyllable2)-1)
        print(aListFiveSyllable[aRandomIndex])
        print(aListSevenSyllable[aRandomIndex])
        print(aListFiveSyllable2[aRandomIndex])
# --- Put your main program below! ---
def main():
    for i in range (1):
        intro()
        user_name = input("Whats your name?")
        say_hello(user_name)
        answer = input("How are you feeling?")
        print("Okay!")
        answer = input("Wanna here a joke?(yes or no)")
        if answer == "yes":
            print("aight!")
            answer = input ("What do you call a guy with a rubber toe?")
            print("ROBERTOOOOOOO")
            print("ahahahahahahaha...sorry if it was bad")
        else:
            print("aww that's no fun")
        answer = input ("Do you want me to generate your meal?(yes or no)")
        if answer == "yes":
            menugenerator()
            print("You are welcome!")
        else:
            print("Okay fine!")
        answer = input ("Do you want me to generate a haiku? (yes or no)")
        if answer == "yes":
            haikugenerator()
        else:
            print("aight your choice")
        answer = input("Im getting a little bit tired, but thanks for taking with me! BYEEE!")
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()



# def intro(name):
#     my_name = name
#     return my_name
# def turn(result):
#     if result == "emily":
#         print("go left")
#     else:
#         print("go right")
#
# turn(intro("emily"))
