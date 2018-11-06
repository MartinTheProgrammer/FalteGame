'''
RaceE Module
'''

import falteStatMod
import falteRaceMod

falteStatMod.mainS()
falteRaceMod.mainR() 

def mainE():
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
                    delay_print("You see a tunic, a belt, a pair of boots and some pants.")
                    responseD = input("Would you like to equip these items?\n")
                    if (responseD == responseY):
                        delay_print("You quickly put on the articles of clothing.")
                        delay_print("You are now clothed.")
                    elif (responseD == responseN):
                        delay_print("Even after inspection, you think it best to leave the clothes alone.")
                        delay_print("You remain naked.")
                elif (responseC == responseN):
                    delay_print("You believe it best to not trust what you see.")
                    delay_print("You remain naked.")
            while (responseB == responseN):
                if (responseB == responseN):
                    delay_print("You decide to stay lying down.")
                    delay_print("You hear the footsteps of people outside. They are heavy and metal.\n")
                    delay_print("They are Elven soldiers.")
    elif (responseA == responseN):
        delay_print(gameOverA)
