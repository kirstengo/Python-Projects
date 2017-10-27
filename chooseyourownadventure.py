import turtle
import time
t = turtle.Turtle()
p = turtle.Turtle()
t.hideturtle()
t.penup()
p.hideturtle()
p.penup()
wn = turtle.Screen()


def title():
    t.write("Exploring the Temple: A Choose your own Adventure!", align="center", font = ("Arial", 30, "normal"))
    time.sleep(2)
    t.clear()
    t.write("\nYou are an adventurer that enjoys exploring temples." "\n One day, you go on one of your expeditions\n"
           "and find a treasure. Unfortunately, you got lost in the temple, \n"
            "but you do have some supplies with you. \n"
            "Can you make it out of the temple? \n" "Good Luck!", align="center", font = ("Arial", 30, "normal") )
    time.sleep(5)
    t.clear()
title()

t.write("\nWhich way do you want to go?",  align="center", font = ("Arial", 30, "normal"))
p.goto(0, -100)
p.write("1. Left  2. Right  ", align="center", font = ("Arial", 30, "normal"))
choice = input("Enter the number of your choice: ")

1

def left():
    p.clear()
    t.clear()
    t.write("\n You hear the sound of water rushing. In front of you, there is a waterfall.\n"
            "You decide to drink from the waterfall and refill your water bottle since the water looks clean. \n"
            "You also see a treasure chest on the ground. Would you like to open it?"
            , align="center", font=("Arial", 30, "normal"))
    p.write("\n 1. Yes  2. No", align="center", font=("Arial", 30, "normal"))
    decision = input("Enter the number of your choice: ")
    if decision == 1:
        p.clear()
        t.clear()
        t.write("\nYou bend down to open the chest.\n"
                "Before you can open it, a strong pineapple falls from the ceiling and hits your head! \n"
                "You die as a result of your injuries. Game Over!", align="center", font=("Arial", 30, "normal"))
        p.write("\n Click the window to close the game and rerun the code to try again.", align="center",
                font=("Arial", 30, "normal"))
    elif decision == 2:
        p.clear()
        t.clear()
        t.write("\n You decide to not open the treasure chest. That chest seemed really suspicious anyway.  \n"
                "There is nothing else in this room, so you decide to leave. \n"
                "Where do you want to go?", align="center", font=("Arial", 30, "normal"))
        p.write("\n  1. Left  2. Right", align="center",
                font=("Arial", 30, "normal"))
        selection = input("Enter the number of your choice: ")
        if selection == 2:
            p.clear()
            t.clear()
            t.write("\n You enter and hear a loud boom. Suddenly, a large boulder begins rolling toward you. \n"
                    "You run as fast as you can, but the boulder rolls you over and squishes you to death. \n"
                    "Game Over!", align="center", font=("Arial", 30, "normal"))
            p.write("\n Click the window to close the game and rerun the code to try again.", align="center",
                    font=("Arial", 30, "normal"))
        elif selection == 1:
            p.clear()
            t.clear()
            t.write("\n You see a long bridge over a large chasm. Walking slowly, you begin crossing the bridge. \n"
                    "Fortunately, you have made it safely to the other side.\n" "You wonder what will happen as "
                    "you enter the next room.", align="center", font=("Arial", 30, "normal"))
            time.sleep(5)
            t.clear()


def right():
    p.clear()
    t.clear()
    t.write("\n You see a large, colorful fruit on the ground. It looks a hybrid of other fruits you like to eat.\n"
         "It looks juicy and delicious. Would you like to eat it?", align="center", font=("Arial", 30, "normal"))
    p.write("\n 1. Sure! Why not?  2. No, I am not that hungry", align="center", font=("Arial", 30, "normal"))
    preference= input("Enter the number of your choice: ")
    if preference == 1:
        p.clear()
        t.clear()
        t.write("\nYou eat the fruit. It tasted great and was very juicy.\n"
        "At least you are no longer hungry or thirsty. Where do you want to go next?", align="center", font=("Arial", 30, "normal"))
        p.write("\n 1. Left  2. Right", align="center", font=("Arial", 30, "normal"))
        pick = input("Enter the number of your choice: ")
        if pick == 1:
            p.clear()
            t.clear()
            t.write("\n As you enter the room, you find yourself stepping on a hidden switch.\n"
                     "The ceiling begins to rumble and spikes begin raining from the ceiling.\n"
                "You die after being impaled by a spike. Game Over!", align="center", font=("Arial", 30, "normal"))
            p.write("\n Click the window to close the game and rerun the code to try again.", align="center",
                    font=("Arial", 30, "normal"))
        if pick == 2:
            p.clear()
            t.clear()
            t.write("\n As you enter the room, you find that there is a large pool of water.\n"
                    "Luckily, you know how to swim and you make it to the other side.\n"
                    "After you dry yourself, you decide it is time to move forward.\n"
                    "Where would you like to go?", align="center", font=("Arial", 30, "normal"))
            p.write("\n 1. Left   2. Right", align="center",
                    font=("Arial", 30, "normal"))
            selection= input("Enter the number of your choice: ")
            if selection == 2:
                p.clear()
                t.clear()
                t.write("\n The room you are in is completely dark. You carefully take a few steps forward. \n"
                        "Suddenly, you can no longer feel the floor beneath you.\n"
                        "You fall a great distance to your death. Game Over!" , align="center", font=("Arial", 30, "normal"))
                p.write("\n Click the window to close the game and rerun the code to try again.", align="center",
                        font=("Arial", 30, "normal"))

            if selection == 1:
                p.clear()
                t.clear()
                t.write("\n You see a long bridge over a large chasm. Walking slowly, you begin crossing the bridge. \n"
                        "Fortunately, you have made it safely to the other side.\n" "You wonder what will happen as "
                        "you enter the next room.", align="center", font=("Arial", 30, "normal"))
                time.sleep(5)
                t.clear()
if choice == 1:
    left()
if choice == 2:
    right()


def troll():
    p.clear()
    t.clear()
    t.write("\n You've been wandering in the temple for a while now. \n"
            "You hope that you are on the right path to the exit.\n"
            "You get the feeling that you are almost at the exit. \n"
            " You walk carefully into the next room", align="center", font=("Arial", 30, "normal"))
    time.sleep(5)
    t.clear()
    t.write("\n There is a large, grumpy troll. He will only let you pass if you give him your food. \n"
            "Since your rations are limited, you cannot give him any.\n"
            "What do you want to do?", align="center", font=("Arial", 30, "normal"))
    p.write("\n 1. Fight the troll with your bare hands! 2. Throw a heavy rock!", align="center",
            font=("Arial", 30, "normal"))
    fight = input("Enter the number of your choice: ")
    if fight == 1:
        p.clear()
        t.clear()
        t.write("\n You begin punching the troll. However, they have no effect on him! \n"
                "The troll eventually overpowers you and picks you up with his hand.\n"
                "He throws you on the ground to your death. Game Over! \n"
                , align="center", font=("Arial", 30, "normal"))
        p.write("\n Click the window to close the game and rerun the code to try again.", align="center",
                font=("Arial", 30, "normal"))
    if fight == 2:
        p.clear()
        t.clear()
        t.write("\n You pick up a heavy rock next to you with all of your strength. \n"
                "You throw it at the troll with all of your might.\n"
                "It is powerful enough to knock the troll unconscious!\n"
                "\n You venture forward into the doorway the troll was blocking"
                , align="center", font=("Arial", 30, "normal"))
        time.sleep(5)
        t.write("\n Yay! You made it outside of the temple! \n"
                "It's been forever since you've seen the daylight!\n"
                "You have won the game!\n"
                , align="center", font=("Arial", 30, "normal"))

troll()
wn.exitonclick()
