'''
RaceH Module
'''

import falteStatMod
import falteRaceMod

falteStatMod.mainS()
falteRaceMod.mainR()
 
def mainH():
    if (race == raceH):
        delay_print("Right. You remember that you are a Human.")
        delay_print(" You are now aware of your race.\n")
        responseA = input("Are you fine will all of  your choices?\n")
        if (responseA == responseY):
            delay_print("You wake up on a bed of straw in a military encampment. There is a crate next to you with some clothes on it's surface.")
            responseB = input("Would you like to get up?\n")
            if (responseB == responseY):
                delay_print("You ease yourself up onto your feet.")
                delay_print("You hear horses, soldiers and common folk alike. None of them seem to notice you.")
                responseC = input("Would you like to inspect the articles of clothing on the crate?\n")
                if (responseC == responseY):
                    delay_print("You see a tunic, a belt, a pair of old boots and a pair of pants.")
                    responseD = input("Would you like to equip these items?\n")
                    if (responseD == responseY):
                        delay_print("You quickly put the articles of clothing on.")
                        delay_print("You are now clothed.")
                    elif (responseD == responseN):
                        delay_print("Even after close inspection, you decide it better to leave the clothes be.")
                        delay_print("You remain naked.")
                elif (responseC == responseN):
                    delay_print("You decide to not trust what you see.")
                    delay_print("You remain naked.")
            while (responseB == responseN):
                if (responseB == responseN):
                    delay_print("You decide to stay lying down.")
                    delay_print("You hear horses, soldiers and common folk alike. None of them seem to notice you.")
        elif (responseA == responseN):
            delay_print(gameOverA)
