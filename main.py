import time 
import random
import threading

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

        #Start the bringLife thread which makes things happen in the background
        # Once this executes, the pet in now alive
        thread=threading.Thread(target=self.bringLife)
        thread.start()

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
    
    def bringLife(self):
        while self.getLife()==True:
            time.sleep(1)

            #Poo part
            if self.getAgeSeconds()%(random.randint(30,120))==0:
                print("\nIv'e had a big stinky poo poo\n")
                self.setCleanliness(self.getCleanliness()-1)
                time.sleep(1)
                print("\nCleanliness is now ", self.getCleanliness(),"\n")
                if self.getCleanliness()==0:
                    print("\n\nI DIED IN MY OWN FILTH!!!\n")
                    self.setLife(False)

            # hunger part
            if self.getAgeSeconds()%(random.randint(30,120))==0:
                print("\nMy belly is rumbling\n")
                self.setHunger(self.getHunger()+1)
                print("\nHunger is now ", self.getHunger(),"\n")
                if self.getHunger()>=10:
                    print("\n\nI DIED OF STARVATION!!!\n")
                    self.setLife(False)
            
            # DeFitness part
            if self.getAgeSeconds()%(random.randint(30,120))==0:
                print("\nI am getting weak\n")
                self.setFitness(self.getFitness()-1)
                print("\nFitness is now ", self.getFitness(),"\n")
                if self.getFitness()<=0:
                    print("\n\nI DIED OF A Heart ATTACK!!!\n")
                    time.sleep(1)
                    print("Perhaps if you had have walked me occationally, I would still be here!!")
                    self.setLife(False)

            # Ageing part
            if self.getAgeSeconds()%60==0:
                print("\nIts my birthday!!!\n")
                print("\nI am ", self.getAgeMinutes(),"Years old today/n")
                
               
                if self.getAgeMinutes()==random.randint(10,20):
                    print("\n\nI DIED OF OLD AGE!!!\n")
                    time.sleep(1)
                    print("I LIVED A LONG AND HAPPY LIFE")
                    self.setLife(False)
        
        
# Main code area 
# This is the area where we execute things

#Create and initialise our cyberPet
plop=CyberPet(5,5)

while plop.getLife()==True:


    #Menu

    print("1 for Status")
    print("2 to feed your pet")
    print("3 take your pet for a walk")
    print("4 to clean your pet's living area")
    
    #Input
    menuChoice=input(": ")
    
    if menuChoice=="1":
        print("I Am", plop.getAgeMinutes(), "Years old")
        print("I am ", plop.getHunger(), "hunger")
        print("I am ", plop.getFitness(),"Fitness")
        print("I am ", plop.getCleanliness(), "Cleanliness")
        print("")
        
        time.sleep(1)
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠛⠛⢦⡀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⠀⠀⠀⠈⣧")
        print("⠀⠀⠀⠀⠀⢀⣠⠴⠞⠛⠉⠉⠉⠉⠉⠉⠛⠒⠾⢤⣀⠀⣀⣠⣤⣄")
        print("⠀⠀⠀⣠⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢭⡀⠀⠈⣷")
        print("⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⢀⡟")
        print("⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡅")
        print("⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⣀")
        print("⣾⠀⠀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣄⠀⠀⠀⠀⠀⠀⠸⡇⠉⣷")
        print("⣿⠀⠰⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣧⡴⠋")
        print("⣿⠀⠀⢸⠛⢫⠀⠀⢠⠴⠒⠲⡄⠀⠀⠀⠀⡝⠛⢡⠀⠀⠀⠀⠀⠀⢰⡏")
        print("⢸⡄⠀⢸⡀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⠀⠀⠀⠀⠀⠀⡼⣄")
        print("⢳⡄⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⢸⠀⠀⠀⠀⢀⡼⠁⢸⡇")
        print("⠀⠀⠙⢦⣷⡈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠈⡇⠀⣀⡴⠟⠒⠚⠋")
        print("⠀⠀⠀⠀⠈⠛⠾⢤⣤⣀⣀⡀⠀⠀⠀⠀⣀⣈⣇⡤⣷⠚⠉")
        print("⠀⠀⠀⠀⠀⠀⠀⣰⠇⠀⠩⣉⠉⠉⠉⣩⠍⠁⠀⢷⣟")
        print("⠀⠀⠀⠀⠀⠀⠀⡟⠐⠦⠤⠼⠂⠀⠸⠥⠤⠔⠂⠘⣿⣇")
        print("⠀⠀⠀⠀⠀⠀⣸⣧⡟⠳⠒⡄⠀⠀⠀⡔⠲⠚⣧⣀⣿⠿⠷⣶⡆")
        print("⠀⠀⠀⠀⠀⠀⠻⣄⢀⠀⠀⡗⠀⠀⠀⡇⠄⢠⠀⣼⠟⠀⢀⣨⠇")
        print("⠀⠀⠀⠀⠀⠀⠀⠙⢶⠬⠴⢧⣤⣤⣤⣽⣬⡥⠞⠛⠛⠋⠉")

    elif menuChoice=="2":
        print("Here's some food for you..")
        time.sleep(1)
        if plop.getHunger() >0:
            print("Nom Nom Nom")
            time.sleep(1)
            print("Nom, slurp, BURRRRP!\n\n")        
            time.sleep(1)
            if plop.getHunger()>0:
                plop.setHunger(plop.getHunger()-1)
            print("Hunger level is now ", plop.getHunger())
            time.sleep(1)
        else:
            print("\nThanks, but I couldnt eat another thing!!!\n")
            time.sleep(1)

    elif menuChoice =="3":
        print("\nYou go for the lead. Your pet hears you and lifts his head\n")
        time.sleep(1)
        print("\nYou take your pet for a nice long walk\n")
        if plop.getFitness()<10:
            plop.setFitness(plop.getFitness()+1)
        else:
            print("I Cannot get any fitter. I am like an olympian\n")
        print("I am ", plop.getFitness(), "fitness")
        time.sleep(2)

        print(" ")

    elif menuChoice=="4":
        print("You enter with a shovel, bucket and mop")
        print("You shovel a poo up and place it in the bin")
        if plop.getCleanliness() >=8:
            print("You get the mop out and finish cleaning the place up")
            print("The place is spick and span now!")
        if plop.getCleanliness()<10:
            plop.setCleanliness(plop.getCleanliness()+1)
        time.sleep(1)
        print(" ")
        
    else:
        print("I do not have that option")
        time.sleep(1)
        print(" ")

