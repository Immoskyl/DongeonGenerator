# -*- coding: utf-8 -*-
import random
import os.path


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#MODIFY VALUES AT WILL

#how many rooms do you want to create?
numberOfRoomToGenerate = 10

#write a file name to create a file containing the script output
fileToSaveDataTo = ""

#change values to modify maximum number of 'special' rooms
maximumOfRoomPerType = dict(SpecialHostileFightersRoom = 1,
                            VictimeRoom = 1,
                            RebelRoom = 1,
                            VisitorRoom = 1,
                            DeceiverRoom = 1,
                            BossRoom = 1)

#set to True if you want to create undifined number of rooms until a Boss Room is created.
#if set to True, it will automatically override the maximumOfRoomPerType[BossRoom] to AT LEAST one
#if set to True, it will still create A MINIMUM OF the amount of rooms set in numberOfRoomToGenerate
createRoomsUntilBoss = False

#LET THIS UNTOUCHED IF YOU'RE NOT SURE OF WHAT YOU'RE DOING
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

roomOccurences = dict(SpecialHostileFightersRoom = 0,
                      VictimeRoom = 0,
                      RebelRoom = 0,
                      VisitorRoom = 0,
                      DeceiverRoom = 0,
                      BossRoom = 0)

def getDice():
    firstVal = random.randint(1,6)
    secondVal = random.randint(1,6)
    if firstVal == secondVal:
        return firstVal*2, True
    return firstVal + secondVal, False


def getCard():
    return random.randint(1,14), random.randint(1,4)


def generatePopulation(diceValue, cardValue):
    inhabitants = min(diceValue, cardValue)
    totalValue = diceValue + cardValue
    text = "Is occupied by "

    if totalValue <= 10:
        return "Is emppy"
    if totalValue <= 12:
        return text + str(inhabitants) + " inhabitants"
    if totalValue <= 14:
        return text + str(inhabitants) + " hostile fighters"
    if totalValue == 15:
        return text + "1 special hostile fighter and " + str(inhabitants) + " potential allies"
    if totalValue == 16:
        return text + "1 special ally and "+ str(inhabitants) + " special fighters"
    if totalValue == 17:
        return text + str(inhabitants/2) + " wandering monters"
    if totalValue == 18:
        if roomOccurences["SpecialHostileFightersRoom"] < maximumOfRoomPerType["SpecialHostileFightersRoom"]:
            roomOccurences["SpecialHostileFightersRoom"] += 1
            return text + str(inhabitants/2) + " special hostile fighters"
        return None
    if totalValue == 19:
        if roomOccurences["VictimeRoom"] < maximumOfRoomPerType["VictimeRoom"]:
            roomOccurences["VictimeRoom"] += 1
            return text + "1 victime"
        return None
    if totalValue == 20:
        if roomOccurences["RebelRoom"] < maximumOfRoomPerType["RebelRoom"]:
            roomOccurences["RebelRoom"] += 1
            return text + "1 rebel inhabitant"
        return None
    if totalValue == 21:
        if roomOccurences["VisitorRoom"] < maximumOfRoomPerType["VisitorRoom"]:
            roomOccurences["VisitorRoom"] += 1
            return text + str(inhabitants) + " visitors"
        return None
    if totalValue == 22:
        if roomOccurences["DeceiverRoom"] < maximumOfRoomPerType["DeceiverRoom"]:
            roomOccurences["DeceiverRoom"] += 1
            return text + "1 deceiver"
        return None
    if roomOccurences["BossRoom"] < maximumOfRoomPerType["BossRoom"]:
        roomOccurences["BossRoom"] += 1
        return text + " the boss and "+ str(inhabitants) + " inhabitants"
    return None


def generateSurroundings(cardColor):
    text = " and usually used for "

    if cardColor == 1:
        return text + "Ressources (farming, warehousing, equipment, constructions...)."
    if cardColor == 2:
        return text + "Rest (sleeping, feeding, playing, healing, praying...)."
    if cardColor == 3:
        return text + "War (training, patrolling, fighting...)."
    return text + "Defenses (barricades, embushes, watch...)."


def generateParticularity(cardValue):
    if cardValue == 10:
        text = "A trap or an obstacle"
    elif cardValue == 11:
        text = "Gear, weapons or equipment"
    elif cardValue == 12:
        text = "A precious object with special properties"
    elif cardValue == 13:
        text = "A real treasure"
    elif cardValue == 14:
        text = "Some revelation or a secret of the World"
    else:
        return ""
    return text + " can be found inside."



def generateActivity(diceValue):
    return generateActivityForOccupiedRoom(diceValue) + generateActivityForEmptyRoom()


def generateActivityForOccupiedRoom(diceValue):
    val = diceValue/2
    text = "The inhabitants of the room may rather be "

    if val == 1:
        return text + "dead"
    if val == 2:
        return text + "ill or injured"
    if val == 3:
        return text + "on the verge of loosing a fight"
    if val == 4:
        return text + "at the orders of an outside force"
    if val == 5:
        return text + "doing something unexpected"
    return text + "well settled ready for a fight"


def generateActivityForEmptyRoom():
    val = random.randint(1,6)
    text = " or be with "

    if val == 1:
        return text + "a mysterious link with a PC."
    if val == 2:
        return text + "a natural hazard (gaz, lava, rockfall...)."
    if val == 3:
        return text + "an escape, a secret passage, a portal..."
    if val == 4:
        return text + "an allegedly magic item or malediction."
    if val == 5:
        return text + "an enigma or a supernatural event."
    return text + " the traces of recent fightings."


def generateRoom():
    diceValue, isItADouble = getDice()
    cardValue, cardColor = getCard()
    textLines = []

    populationText = generatePopulation(diceValue, cardValue)
    if populationText is None:
        return generateRoom()

    textLines.append(populationText)
    textLines[-1] += generateSurroundings(cardColor)

    particularityText = generateParticularity(cardValue)
    if particularityText:
        textLines.append(particularityText)
    if isItADouble:
        textLines.append(generateActivity(diceValue))
    textLines.append("")
    return textLines


def printRoomInfos(roomInfos):
    for line in roomInfos:
        print line


def generateKeep(totalNumberOfRoom):
    createRoomsUntilBossCondition = createRoomsUntilBoss
    keepInfos = []
    i = 0
    while i < totalNumberOfRoom or createRoomsUntilBossCondition:
        roomInfos = ["Room #" + str(i + 1) + ": "]
        roomInfos += generateRoom()
        keepInfos += roomInfos
        printRoomInfos(roomInfos)
        createRoomsUntilBossCondition = createRoomsUntilBoss and not roomOccurences["BossRoom"]
        i += 1
    return keepInfos


def createNewSaveFileName(fileName):
    parts = fileName.rsplit(".")
    baseFileName = parts[0]
    try:
        extension = parts[1]
    except:
        extension = ""

    try:
        baseFileName = baseFileName[:-2] + str(int(baseFileName[-2]) + 1) + baseFileName[-1:]
    except:
        baseFileName += " (2)"

    return baseFileName + "." + extension


def saveInfosToFile(infos, fileName):
    if os.path.exists(fileName):
        saveInfosToFile(infos, createNewSaveFileName(fileName))
        return
    file = open(fileName, "w")
    for line in infos:
        file.write(line + "\n")
    print "You have chosen to save the generation. The file " + str(fileName) + " has been successfully created."


def prepareSettings():
    if createRoomsUntilBoss:
        prepareCreateRoomsUntilBoss()


def prepareCreateRoomsUntilBoss():
    if maximumOfRoomPerType["BossRoom"] == 0:
        maximumOfRoomPerType["BossRoom"] = 1


def main():
    prepareSettings()
    keepInfos = generateKeep(numberOfRoomToGenerate)
    if fileToSaveDataTo:
        saveInfosToFile(keepInfos, fileToSaveDataTo)

main()
