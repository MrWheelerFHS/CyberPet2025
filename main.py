import time 
import random

# Cyber pet class
class CyberPet:
    #Class attributes
    __birthTime=time.time()
    __life=True
    __cleanliness = random.randint(1,10)

    
    #The constructor method
    def __init__(self, hunger, fitness):
        self.__fitness=fitness
        self.__hunger=hunger

    #Instance methods
    def getHunger(self):
        return self.__hunger
    def setHunger(self, hunger):
        self.__hunger = hunger

    def getFitness(self):
        return self.__fitness
    def setFitness(self, fitness):
        self.__fitness = fitness
    # Returns how many seconds the pet is old
    def getAgeSeconds(self):
        return int(time.time()-self.__birthTime) 
    # Returns how many seconds the pet is old
    def getAgeMinutes(self):
        return int((time.time()-self.__birthTime)//60) 
    #sets and gets the life status of the pet
    def getLife(self):
        return self.__life
    def setLife(self, life):
        self.__life=life
    def getCleanliness(self):
        return self.__cleanliness
    def setCleanliness(self, cleanliness):
        self.__cleanliness=cleanliness
        
        


def badStuff():
    while plop.getLife()==True:
        time.sleep(1)
        if plop.getAgeSeconds()%10==0:
            print("poo")
# Main code area 
# This is the area where we execute things

plop=CyberPet(5,5)
plop.setHunger(plop.getHunger()-1)

while True:
    #Menu

    print("1 for Status")
    print("2 for Fitness")
    print("3 for Cleanliness")
    print("4 for Hunger")
    
    #Input
    menuChoice=input(": ")
    
    if menuChoice=="1":
        print("I Am", plop.getAgeMinutes(), "Years old")
        print("I am ", plop.getFitness(),"Fitness")
        print("I am ", plop.getCleanliness(), "Cleanliness")
        print("I am ", plop.getHunger(), "hunger")
        time.sleep(1)
        print(" ")
    elif menuChoice=="2":
        print("I am ", plop.getFitness(),"Fitness")
        time.sleep(1)
        print(" ")
    elif menuChoice =="3":
        print("I am ", plop.getCleanliness(), "Cleanliness")
        time.sleep(1)
        print(" ")
    elif menuChoice=="4":
        print("I am ", plop.getHunger(), "hunger")
        time.sleep(1)
        print(" ")
    else:
        print("I do not have that option")
        time.sleep(1)
        print(" ")

