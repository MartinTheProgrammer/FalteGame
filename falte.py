'''
    Software Engineer: Martin Belt
    Date: 10/14/18
    Time: 6:47 PM CST
    Program: txt.exe

    Co-Developer: William G. F. Downing
    Joined: 10/25/18
    Time: 9:05 AM CST

    Renamed: falte.py
    Date: 10/30/18
    Time: 11:27 AM CST

    Rewritten Code: Alpha (version 1.2.1)
    Date: 10/30/18
    Time: 9:06 PM CST
'''
import time
import random
import sys
import raceEMod
import raceDMod
import raceHMod

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)

gameOverA = "Game Over."
gameOverB = "You have perished. Game Over."

health = 100
mana = 100

oStrength = random.randint(50, 100)
oDexterity = random.randint(50, 100)
oWillpower = random.randint(50, 100)
oAgility = random.randint(50, 100)

Strength = oStrength
Dexterity = oDexterity
Willpower = oWillpower
Agility = oAgility

raceList = ['Elf', 'Dwarf', 'Human']

raceE = "Elf"
raceD = "Dwarf"
raceH = "Human"

genderM = "Male"
genderF = "Female"

responseY = "Yes"
responseN = "No"

print("Health: ", health)
print("Mana: ", mana)

print("Strength: ",  Strength)
print("Dexterity: ", Dexterity)
print("Willpower: ", Willpower)
print("Agility: ", Agility)
print("--------------------------------------------------------------------------------------------------------------")
print("\n")
delay_print("You are surrounded by darkness. You see nothing. You can't move.\n")
delay_print("You don't remember what you look like.")
gender = input(" What is your gender? (Male or Female)\n")
if (gender == genderM):
    delay_print("Yes. You remember your manly muscles and all the rest of your masculinity.")
    delay_print(" You are now aware of your gender.\n")
    delay_print("You remember that there are three different races in your country of birth, Falte.\n")
    print("\n")

    for i in range(0, 3):
        print(raceList[i] + "\n")

    race = input("What is your race?\n")
    if (race == raceE):
        raceEMod.mainE() 

    elif (race == raceD):
        raceDMod.mainD()

    elif (race == raceH):
        raceHMod.mainH()

elif (gender == genderF):
    delay_print("Yes. You remember your feminine charms and intuition.")
    delay_print(" You are now aware of your gender.\n")
    delay_print("You remember that there are three different races in your country of birth, Falte.\n")
    print("\n")

    for i in range(0, 3):
        print(raceList[i] + "\n")

    race = input("What is your race?\n")
    if (race == raceE):
        delay_print("Right. You remember that you are an Elf.")
        delay_print(" You are now aware of your race.\n")
        responseA = input("Are you fine will all of  your choices?\n")
        if (responseA == responseY):
            delay_print("You wake up on a cot in a tent. There is a desk next to you with some clothes on it's surface.")
            responseB = input("Would you like to get up?\n")
            if (responseB == responseY):
                delay_print("You ease yourself up onto your feet.")
                delay_print("Your balance is poor at the moment. You hear the footsteps of people outside. They are heavy and metal.\n")
                delay_print("They are Elven soldiers.")
                responseC = input("Would you like to inspect the articles of clothing on the desk?\n")
                if (responseC == responseY):
                    delay_print("A dress, a pair of boots and a corsette lie in front of you.")
                    responseD = input("Would you like to equip these articles of clothing?\n")
                    if (responseD == responseY):
                        delay_print("You quickly put on the clothes.")
                        delay_print("You are now clothed.")
                    elif (responseD == responseY):
                        delay_print("Even with closer inspection, you decide that it is better if you leave the clothes alone.")
                        delay_print("You remain naked.")
                elif (responseC == responseN):
                    delay_print("You decide to not trust what you see.")
                    delay_print("You remain naked.")
            while (responseB == responseN):
                if (responseB == responseN):
                    delay_print("You decide to stay lying down.")
                    delay_print("You hear the footsteps of people outside. They are heavy and metal.\n")
                    delay_print("They are Elven soldiers.")
        elif (responseA == responseN):
            delay_print(gameOverA)
    
    elif (race == raceD):
        delay_print("Right. You remember that you are a Dwarf.")
        delay_print(" You are now aware of your race.\n")
        responseA = input("Are you fine will all of  your choices?\n")
        if (responseA == responseY):
            delay_print("You wake up on a bunk in a bunkhouse. There is a table next to you with some clothes on it's surface.")
            responseB = input("Would you like to get up?\n")
            if (responseB == responseY):
                delay_print("You ease yourself up onto your feet.")
                delay_print("You are alone in this room. You hear nothing outside of the walls.\n")
                responseC = input("Would you like to inspect the articles of clothing on the table?\n")
                if (responseC == responseY):
                    delay_print("There is a dress, a corsette and a pair of boots in front of you.")
                    responseD = input("Would you like to equip the articles of clothing in front of you?\n")
                    if (responseD == responseY):
                        delay_print("You quickly equip the articles of clothing.")
                        delay_print("You are now clothed.")
                    elif (responseD == responseN):
                        delay_print("Even with closer inspection, you decide to leave the clothes alone.")
                        delay_print("You remain naked.")
                elif (responseC == responseN):
                    delay_print("You decide that it is best if you don't poke around things that aren't exactly yours.")
                    delay_print("You remain naked.")
            while (responseB == responseN):
                if (responseB == responseN):
                    delay_print("You decide to stay lying down.")
                    delay_print("You are alone in this room. You hear nothing outside of the walls.\n")
        elif (responseA == responseN):
            delay_print(gameOverA)

    elif (race == raceH):
        delay_print("Right. You remember that you are a Human.")
        delay_print(" You are now aware of your race.\n")
        responseA = input("Are you fine will all of  your choices?\n")
        if (responseA == responseY):
            delay_print("You wake up on a bed of straw in a military encampment. There is a crate next to you with some clothes on it's surface.")
            responseB = input("Would you like to get up?\n")
            if (responseB == responseY):
                delay_print("You ease yourself up onto your feet.")
                delay_print("You hear horses, soldiers and common folk alike. None of them seem to take any notice of you.\n")
                responseC = input("Would you like to inspect the articles of clothing on the crate?\n")
                if (responseC == responseY):
                    delay_print("Lying in front of you is a dress, a corsette and an old pair of boots.")
                    responseD = input("Would you like to equip the articles of clothing in front of you?\n")
                    if (responseD == responseY):
                        delay_print("You quickly put on the clothes.")
                        delay_print("You are now clothed.")
                    elif (responseD == responseN):
                        delay_print("Even with closer examination, you decide that it is best to leave the clothes alone.")
                        delay_print("You remain naked.")
                elif (responseC == responseN):
                    delay_print("You decide that you shouldn't wear them.")
                    delay_print("You remain naked.")
            while (responseB == responseN):
                if (responseB == responseN):
                    delay_print("You decide to stay lying down.")
                    delay_print("You hear horses, soldiers and common folk alike. None of them seem to take any notice of you.\n")
        elif (responseA == responseN):
            delay_print(gameOverA)
