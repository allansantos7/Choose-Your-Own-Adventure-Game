# Allan Delos Santos
# CS 3620
# Project 1

# include random library for use of our encounter variables
import random

# global variables
randomEnc = 0
randomNum = 0

# choice variables
choiceSector = 0
choiceAction = 0
choicesLeft = 3


# enemy class
class Ship():
    def __init__(self, name, HP, dmg, Fuel):
        self.name = name
        self.HP = HP
        self.dmg = dmg
        self.Fuel = Fuel

    def displayName(self):
        print(self.name)

    def displayHP(self):
        print(self.name + " HP: \n")
        print(self.HP)

    def returnHP(self):
        return self.HP

    def subtractHP(self, dmg):
        self.HP -= dmg
        self.displayHP(self)

    def dealDMG(self, enemyName, dmg):
        print(enemyName.name + " takes " + str(dmg) + " DMG.")
        enemyName.HP -= dmg
        enemyName.displayHP(enemyName)



class ScoutDrone(Ship):
    name = "Unmanned Scout Drone"
    HP = 10

    def calcDMG(self):
        self.dmg = random.randint(1, 3)
        return self.dmg


class RebelInterceptor(Ship):
    name = "RebelInterceptor"
    HP = 25

    def calcDMG(self):
        self.dmg = random.randint(1, 5)
        return self.dmg


class PirateInterceptor(Ship):
    name = "PirateInterceptor"
    HP = 20

    def calcDMG(self):
        self.dmg = random.randint(1, 3)
        return self.dmg


class User(Ship):
    name = "Federation Scout"
    HP = 20
    Fuel = 20

    def displayStatus(self):
        if self.HP <= 0:
            userDeath()

        print(self.name + " HP: \n")
        print(self.HP)
        print("\nCurrent Fuel: \n")
        print(self.Fuel)
        print("\n")

    def calcDMG(self):
        self.dmg = random.randint(1, 5)
        return self.dmg

    def addFuel(self, Fuel):
        print("Your ship gains: " + str(Fuel) + " Fuel.")
        self.Fuel += Fuel

        if self.Fuel > 20:
            self.Fuel = 20

    def subtractFuel(self, Fuel):
        print("Your ship uses: " + str(Fuel) + " Fuel.")
        self.Fuel -= Fuel

        if self.Fuel <= 0:
            userEmptyFuel()

    def addHP(self, HP):
        print("Your ship restores: " + str(HP) + " HP.")
        self.HP += HP

        if self.HP > 20:
            self.HP = 20


    def subtractHP(self, dmg):
        self.HP -= dmg

        if self.HP <= 0:
            userDeath()

        self.displayHP(self)


# functions


def tutorialIntro():
    print("Let's display your status: \n")
    User.displayStatus(User.HP, User.Fuel)
    print("I'm sure you can imagine what happens when your ship's HP or Hull Points reaches 0.\n")
    print("The drawback to the ship's speed and evasion is the need to balance a resource called Fuel.\n")
    print("You can only hold up to 20 Fuel at one time.\n")
    print("If your fuel runs out, you're stranded. This is a covert mission, you must reach Federation HQ!\n")
    print(
        "Also, to travel from sector to sector, an exit beacon provides your ship's engines with enough force for FTL "
        "travel between sectors.\n")
    print("Without the beacon, you are stuck on that sector you're currently on...\n")
    return


# prompt what user would like to do in current sector
def userPrompt():
    global choiceAction
    choiceAction = 0

    if choicesLeft <= 0:
        print("With nothing left to explore in the sector, you look for the exit beacon.\n")
        foundExit()
        exit

    while choiceAction not in (1, 2):
        try:
            choiceAction = int(input("What would you like to do: \n" + str(userActions12) + "\n"))

        except ValueError:
            print("Invalid Input")

    return choiceAction


# pass in choice, either explore or look for beacon
# random number determine what is encountered, number is adjusted depending the sector
def userActionChoice(choice):
    global choicesLeft

    if choice == 1:
        User.subtractFuel(User, 2)
        print("You have decided to explore the current sector.")
        global randomEnc
        randomEnc = random.randint(0, 100)
        chanceFuel = 0
        chanceRepair = 0
        chanceTrader = 0

        # encounter variable changes depending on sector
        if choiceSector == 1:
            chanceFuel = 30
            chanceRepair = 60
        elif choiceSector == 2:
            chanceFuel = 25
            chanceRepair = 50
            chanceTrader = 75
        elif choiceSector == 3:
            chanceFuel = 50
            chanceRepair = 10
            chanceTrader = 0
        elif choiceSector == 4:
            chanceFuel = 20
            chanceRepair = 40
            chanceTrader = 50
        else:
            chanceFuel = 50
            chanceRepair = 68
            chanceTrader = 86

        if randomEnc <= chanceFuel:
            foundfuel()

        elif randomEnc <= chanceRepair:
            foundrepair()

        elif randomEnc <= chanceTrader:
            foundtrader()

        else:
            foundEnemy()

        choicesLeft -= 1

        print("\nHaving done all that, you're back to a decision on what next.\n")
        User.displayStatus(User)
        print("Destinations left to explore: " + str(choicesLeft) + "\n")
        userActionChoice(userPrompt())

    else:
        foundExit()

        choicesLeft -= 1



def foundfuel():
    file = open("foundfuel.txt", "r")
    contents = file.read()
    print(contents)
    file.close()

    randomNum = random.randint(1, 10)
    print(str(randomNum) + " Fuel")
    User.addFuel(User, randomNum)


def foundrepair():
    file = open("foundrepair.txt", "r")
    contents = file.read()
    print(contents)
    file.close()

    randomNum = random.randint(1, 10)
    print(str(randomNum) + " HP")
    User.addHP(User, randomNum)


def foundtrader():
    file = open("foundtrader.txt", "r")
    contents = file.read()
    print(contents)
    file.close()

    User.displayStatus(User)

    choiceTrader = 0
    while choiceTrader not in (1, 2, 3):
        try:
            choiceTrader = int(
                input("Choose any selection by typing the number for either: \n" + str(traderChoices) + "\n"))

        except ValueError:
            print("Invalid Input")

    if choiceTrader == 1:
        if User.HP <= 2:
            print("Not enough HP. \nThe trader notices you trying to pull a fast one on them, they shoot you.")
            randomNum = random.randint(0, 2)
            User.subtractHP(User, randomNum)


        else:
            User.addFuel(User, 5)
            User.subtractHP(User, 2)


    elif choiceTrader == 2:
        if User.Fuel <= 2:
            print("Not enough Fuel. \nThe trader notices you trying to pull a fast one on them, they shoot you.")
            randomNum = random.randint(0, 2)
            User.subtractHP(User, randomNum)

        else:
            User.addHP(User, 5)
            User.subtractFuel(User, 2)


    else:
        print("Noticing the scummy prices and the scam artist that they are, you leave.")


def foundExit():
    User.subtractFuel(User, 4)

    print("The beacon you jump to emanates a strange energy.\n "
          "Your ship indicates it can utilize this beacon to jump to the next sector.\n")


# enemy encounter method, randomizes what enemy is encountered between 3 types
def foundEnemy():
    enemyNum = random.randint(0, 2)
    enemyName = enemyTypes[enemyNum]
    userFightChoice = 0

    file = open("enemyType" + str(enemyNum) + ".txt", "r")
    contents = file.read()
    print(contents)
    file.close()

    print("It's fight or flight, what would you like to do: \n"
          "1: Fight\n"
          "2: Tactical Retreat (Run Away) - Costs 6 Fuel\n")

    userFightChoice = int(input(""))

    if userFightChoice == 1:
        combatEnemy(enemyName)

    elif userFightChoice == 2 and enemyName == "ScoutDrone":
        file = open("escapeDrone.txt", "r")
        contents = file.read()
        print(contents)
        file.close()

        combatEnemy(enemyName)

    else:
        User.subtractFuel(User, 6)
        print("You demonstrate your technical prowess of the ship, muster all your courage,\n"
              " and are able divert as much power as needed to escape.\n")


def combatEnemy(enemyName):
    userFightChoice = 0

    if enemyName == "ScoutDrone":
        Ship.displayName(ScoutDrone)
        Ship.displayHP(ScoutDrone)

        while User.HP > 0 or ScoutDrone.returnHP(ScoutDrone) > 0:
            userFightChoice = 0
            userFightChoice = int(input("Battle Choice:\n"
                                        "1: Fire!\n"))

            print("Fire!")
            User.dealDMG(User, ScoutDrone, User.calcDMG(User))

            if ScoutDrone.returnHP(ScoutDrone) <= 0:
                print("You look at the wreckage of the drone.\n"
                      "For an AI to cause you so much trouble brings a shiver down your spine to what they could be capable of"
                      "in the future.")
                return

            print("The drone returns fire back at ya.")
            ScoutDrone.dealDMG(ScoutDrone, User, ScoutDrone.calcDMG(ScoutDrone))

            if User.HP <= 0:
                userDeath()
                return





    elif enemyName == "RebelInterceptor":
        Ship.displayName(RebelInterceptor)
        Ship.displayHP(RebelInterceptor)

        while User.HP > 0 or RebelInterceptor.returnHP(RebelInterceptor) > 0:
            userFightChoice = 0
            userFightChoice = int(input("Battle Choice:\n"
                                        "1: Fire!\n"
                                        "2: Surrender\n"))

            if userFightChoice == 1:
                print("Fire!")
                User.dealDMG(User, RebelInterceptor, User.calcDMG(User))

                if RebelInterceptor.returnHP(RebelInterceptor) <= 0:
                    print("You look at the wreckage of the Interceptor.\n"
                          "'It was either you or them', you said to yourself.\n"
                          "Neither of you started this war, but you sure are going to finish it.\n"
                          "You shave real quick, then leave.\n")
                    return

                print("The Interceptor returns fire back at ya.")
                RebelInterceptor.dealDMG(RebelInterceptor, User, ScoutDrone.calcDMG(RebelInterceptor))

                if User.HP <= 0:
                    userDeath()
                    return

            else:
                print("You changed your mind, you surrender instead.")
                userSurrender()
                return

    else:
        Ship.displayName(PirateInterceptor)
        Ship.displayHP(PirateInterceptor)

        while User.HP > 0 or PirateInterceptor.returnHP(PirateInterceptor) > 0:
            userFightChoice = int(input("Battle Choice:\n"
                                        "1: Fire!\n"
                                        "2: Surrender\n"))

            if userFightChoice == 1:
                print("Fire!")
                User.dealDMG(User, PirateInterceptor, User.calcDMG(User))

                if PirateInterceptor.returnHP(PirateInterceptor) <= 0:
                    print("You look at the wreckage of the Pirate.\n"
                          "'It's a shame.' They weren't a part of this war. Just a poor fool trying to survive.\n"
                          "In very unethical ways. You begin to ponder life's frailty.\n"
                          "You put away your monocle, fedora, and bubble pipe.\n"
                          "You leave.\n")
                    return

                print("The Interceptor returns fire back at ya.")
                RebelInterceptor.dealDMG(PirateInterceptor, User, ScoutDrone.calcDMG(PirateInterceptor))

                if User.HP <= 0:
                    userDeath()
                    return

            else:
                print("You changed your mind, you surrender instead.")
                userSurrender()


def userEmptyFuel():
    print("Without a care in the world, you used all your fuel. You are now stranded.\n"
          "Instead of realizing the importance of your mission, you treated your most important resource as if it "
          "were as readily available as air (I know you're in space at the moment).\n"
          "Your care for your fuel is one of the most insane idiotic things I've ever seen.\n"
          "At no point in your playthrough, would anyone say you had anything close to a rational decision or thought.\n"
          "You are awarded no points.")
    exit(0)

def userSurrender():
    print("You came to the conclusion that you had no chance to beat this ship, what were you thinking?\n"
          "You decided to power off your weapons and send a message of surrender to the enemy ship\n"
          "The enemy boards and takes everything worty of value, this include the intel from the Rebel base...\n"
          "Game over man. Game over.\n")
    exit(0)


def userDeath():
    print("After sustaining the last amount of damage your hull can take, your ship cracks at the point of it's last"
          " sustained hit.\n"
          "The breach in the hull sucks a majority of your crew into the depths of space.\n"
          "With the majority of the crew gone, "
          "the remaining members are unable to keep up the repairs before it's too late.\n"
          "The ship erupts.\n"
          "Mission Failed, You'll get em next time.\n")
    exit(0)


# collections to store difference locations, choices, encounters, and enemy types
locations12 = {
    1: "Civilian",
    2: "Neutral"
}

locations34 = {
    3: "Asteroid",
    4: "Hostile"
}

locations16 = {
    1: "Civilian",
    6: "Nebula"
}

userActions12 = {
    1: "Explore - Costs 2 Fuel",
    2: "Look for Exit Beacon - Costs 4 Fuel"
}

encounterTypes1234 = {
    1: "Found Fuel",
    2: "Found Repair Ship",
    3: "Found Trader",
    4: "Found Enemy"
}

enemyTypes = ["ScoutDrone", "RebelInterceptor", "PirateInterceptor"]

traderChoices = {
    1: "5 Fuel for 2 HP",
    2: "5 HP for 2 Fuel",
    3: "Leave"
}

combatChoices = {
    1: "Shoot",
    2: "Run"
}

# intro
file = open("intro.txt", "r")
contents = file.read()
print(contents)
file.close()

# first decision, while loop until they enter valid input, check for errors
file = open("location12.txt", "r")
contents = file.read()
print(contents)
file.close()

while choiceSector not in (1, 2):
    try:
        choiceSector = int(input("Choose either sector by typing the number for either: \n" + str(locations12) + "\n"))

    except ValueError:
        print("Invalid Input")

file = open("tutorialSector.txt", "r")
contents = file.read()
print(contents)
file.close()

# civilian sector, user more likely to encounter traders
if choiceSector == 1:

    file = open("civilian.txt", "r")
    contents = file.read()
    print(contents)
    file.close()

    userActionChoice(userPrompt())

    print("It's time to move on to the next sector.")
    file = open("location34.txt", "r")
    contents = file.read()
    print(contents)
    file.close()

    # next sector choice asteroid or hostile
    choicesLeft = 3
    while choiceSector not in (3, 4):
        try:
            choiceSector = int(
                input("Choose either sector by typing the number for either: \n" + str(locations34) + "\n"))

        except ValueError:
            print("Invalid Input")


    if choiceSector == 3:
        file = open("asteroid.txt", "r")
        contents = file.read()
        print(contents)
        file.close()

        userActionChoice(userPrompt())

        print("You move on to the next and last sector.")
        file = open("federation.txt", "r")
        contents = file.read()
        print(contents)
        file.close()

    else:
        file = open("hostile.txt", "r")
        contents = file.read()
        print(contents)
        file.close()

        userActionChoice(userPrompt())

        print("You move on to the next and last sector.")
        file = open("federation.txt", "r")
        contents = file.read()
        print(contents)
        file.close()

# neutral sector, equal chance to encounter all types
else:
    choicesLeft = 3

    file = open("neutral.txt", "r")
    contents = file.read()
    print(contents)
    file.close()

    userActionChoice(userPrompt())

    print("It's time to move on to the next sector.")
    file = open("location16.txt", "r")
    contents = file.read()
    print(contents)
    file.close()

    # next sector choice asteroid or hostile
    choicesLeft = 3
    while choiceSector not in (1, 6):
        try:
            choiceSector = int(
                input("Choose either sector by typing the number for either: \n" + str(locations16) + "\n"))

        except ValueError:
            print("Invalid Input")


    if choiceSector == 1:
        file = open("civilian.txt", "r")
        contents = file.read()
        print(contents)
        file.close()

        userActionChoice(userPrompt())

        print("You move on to the next and last sector.")
        file = open("federation.txt", "r")
        contents = file.read()
        print(contents)
        file.close()

    else:
        file = open("nebula.txt", "r")
        contents = file.read()
        print(contents)
        file.close()

        userActionChoice(userPrompt())

        print("You move on to the next and last sector.")
        file = open("federation.txt", "r")
        contents = file.read()
        print(contents)
        file.close()