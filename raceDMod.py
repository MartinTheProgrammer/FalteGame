'''
RaceD Module
'''

import falteStatMod
import falteRaceMod

falteStatMod.mainS() 
falteRaceMod.mainR()

def mainD():
    if (race == raceD):
        delay_print("Right. You remember that you are a Dwarf.")
        delay_print(" You are now aware of your race.\n")
        responseA = input("Are you fine will all of  your choices?\n")
        if (responseA == responseY):
            delay_print("You wake up on a bunk in a bunkhouse. There is a table next to you with some clothes on it's surface.")
            responseB = input("Would you like to get up?\n")
            if (responseB == responseY):
                delay_print("You ease yourself up onto your feet.")
                delay_print("You are alone in this room. You hear nothing outside of the walls.")
                responseC = input("Would you like to inspect the articles of clothing on the table?\n")
                if (responseC == responseY):
                    delay_print("You see a tunic, a pair of old work boots, a pair of pants and a belt.")
                    responseD = input("Would you like to equip these items?\n")
                    if (responseD == responseY):
                        delay_print("You quickly put on the articles of clothing.")
                        delay_print("You are now clothed.")
                    elif (responseD == responseN):
                        delay_print("Even after certain inspection, you think it best to leave the clothes alone.")
                        delay_print("You remain naked.")
                elif (responseC == responseN):
                    delay_print("You decide to not trust what you see.")
                    delay_print("You remain naked.")
            while (responseB == responseN):
                if (responseB == responseN):
                    delay_print("You decide to stay lying down.")
                    delay_print("You are alone in this room. You hear nothing outside of the walls.")
        elif (responseA == responseN):
            delay_print(gameOverA)
