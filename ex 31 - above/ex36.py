#desigining and debugging
from sys import exit
def main():
    print("Your are in the room A.")
    print("Do you wanna go thorugh door 1 or door 2?")
    
    while True:
        door = input("> ")
        if "1" in door:
            room_b()
        elif "2" in door:
            room_d()
        else:
            print("Wrong Door!!")


def room_b():
    print("You're in room B.")
    print("Do you wanna go through door 1 or door 2 or door 3?")
    
    while True:
        door = input("> ")
        if "1" in door:
            main()
        elif "2" in door:
            room_e()
        elif "3" in door:
            room_c()
        else:
           print("Wrong Door!!")

def room_d():
    print("You're in room D.")
    print("Do you wanna go thorugh door 1 or door 2?")
    
    while True:
        door = input("> ")
        if "1" in door:
            main()
        elif "2" in door:
            room_e()
        else:
            print("Wrong Door!!")

def room_e():
    print("You're in room E.")
    print("Do you wanna go through door 1 or door 2?")
    
    while True:
        door=input("> ")
        if "1" in door:
            room_d()
        elif "2" in door:
            room_b()
        else:
            print("Wrong Door!!")

def room_c():
    print("You're in room C.")
    print("There is only one door.")
    print("Do you want to go back to room B?")
    
    while True:
        response= input("> ").lower()

        if response in ['y','yes']:
            room_b()
        else:
            print("This is the End.")
            exit(0)
main()