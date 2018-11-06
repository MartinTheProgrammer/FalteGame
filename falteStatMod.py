'''
FalteStat Module
'''
import random

def mainS():
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
