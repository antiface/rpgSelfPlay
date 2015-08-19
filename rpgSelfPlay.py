#To build this I used the following references:
#http://www.tutorialspoint.com/python/python_classes_objects.htm
#http://docs.python.org/2/tutorial/classes.html
# and
#http://www.tutorialspoint.com/python/python_dictionary.htm

from random import randint

#A class is an object that has methods and properties. They can be described easily as such:
#A property is something you are, or something you have. In this example your name, class, health, energy, and even a list of actions are properties. When I say action list I'm actually storing them as nested dictionaries. This just means it is a dictionary that the values of each item are actually individual dictionaries as well.
#A method is something you can do. It is a function that the object can perform. The main reason to build a function inside of a class and use it as a method instead of just calling a function and referencing the object is because of 'self'.
#If you notice my function has a required input parameter of 'self' and inside the function it is constantly reading data from and pushing data to 'self'. But when I call that function I never tell it what self is. 'Self' is assumed to be the object that called the method. So, if 'Player' calls performaction, it is assumed that 'Player' is 'self'.
class Character:
    Name = 'Default'
    Class = 'Default'
    Health = 10
    Energy = 10
#Here I am just saying that his variable is a dictionary inside of a dictionary. Because all of my characters have manually defined ActionLists when I make them, no one will actually ever have this default action.
    ActionList = {'Sleep': {'Damage': 0, 'Cost': 0} }

#When I call this function, I will never use 'Self', it is assumed to be the object that called the function. Only objects that are declared with a class of 'Character' can use this function, it isn't available to anything else.
    def PerformAction(self, ActionName, target):
        if (self.Energy -  self.ActionList[ActionName]['Cost']) >= 0:
            print (self.Name + " :")
            print (ActionName + " was used by " + self.Name + " . It dealt " + str(self.ActionList[ActionName]['Damage']) + " to " + target.Name + " and cost " + str(self.ActionList[ActionName]['Cost']) + " Energy.")
            self.Energy -= self.ActionList[ActionName]['Cost']
            target.Health -= self.ActionList[ActionName]['Damage']
            print (self.Name + " has " + str(self.Energy) + " energy remaining. " + target.Name + " has " + str(target.Health) + " health remaining.")
            print ("")
        else:
            print (self.Name + " doesn't have enough energy to perform  " + ActionName + ". " + str(self.ActionList[ActionName]['Cost']) + " is required but only " + str(self.Energy) + " energy is remaining")
            print ("")
            

#I create a new variable named 'Player', first thing I do is declare it is an object of my custom class that I named 'Character'.
Player = Character()
#I then proceed to give it various properties, to change the defaults I left in the class. If I don't specify a value here, it will remain as what it was set to in the class.
Player.Name = 'Tory'
Player.Class = 'Wizzard'
Player.Health = 30
Player.Energy = 20
#This is the nested dictionary. All it really is is a single dictionary with 3 keys: Fireball, Ice Cone, and Kinetic Blast.
#The values assigned to these keys just so happen to be dictionaries also, this means when I display the value of a key, the result will be displaying a whole dictionary key pair.
#You will notice when I use this variable I will use two keys, the first is which spell, the second references if I want to know the damage or the cost of that spell.
Player.ActionList = {'Fireball': {'Damage': 4, 'Cost': 3}, 'Ice Cone': {'Damage': 6, 'Cost': 4}, 'Kinetic Blast': {'Damage': 2, 'Cost': 5}}

#Same thing as before, I'm making a new character, my custom class. This time I am saving that custom object under a different variable.
EnemyA = Character()
EnemyA.Name = 'Freddrick'
EnemyA.Class = 'Lazy Goblin'
EnemyA.Health = 20
EnemyA.Energy = 10
EnemyA.ActionList = {'Swing Club': {'Damage': 1, 'Cost': 1}, 'Loaf around':{'Damage': 0, 'Cost': 0}}

#And same again.
EnemyB = Character()
EnemyB.Name = 'Robert'
EnemyB.Class = 'Very Lazy Goblin'
EnemyB.Health = 20
#Notice I didn't set the energy level for EnemyB, this will cause him to have 10 energy because that is what the class uses by default.
EnemyB.ActionList = {'Throw Club': {'Damage': 3, 'Cost': 2}, 'Loaf around':{'Damage': 0, 'Cost': 0}}

#To save on code and logic checks I'm going to reuse the battle code for both enemies. So I'm going to only fight 'CurrentEnemy' instead of each enemy individually. Right now the 'CurrentEnemy' is going to be EnemyA, when he dies I will switch it over to EnemyB.
CurrentEnemy = EnemyA

while True:
    #Every turn every active fighter gains 1 energy point.
    Player.Energy += 1
    CurrentEnemy.Energy += 1
    if Player.Health <= 0:
        print (Player.Name + " has died, you lose.")
        break
    elif (CurrentEnemy == EnemyA and EnemyA.Health <= 0):
        print (Player.Name + " the " + Player.Class + " has defeated " + EnemyA.Name + " the " + EnemyA.Class + " but next you will face " + EnemyB.Name + " the " + EnemyB.Class + " .")
        print ("")
        CurrentEnemy = EnemyB
    elif (CurrentEnemy == EnemyB and EnemyB.Health <= 0):
        print ("You have defeated all the enemies. You win!")
        break
    else:
        random = randint(0, len(Player.ActionList.keys())-1)
        index = 0
        #Because I want to randomly pick actions, but I used a dictionary that doesn't use a numerical index I had to interate through the actions until I found the one at the index value I wanted.
        #I'm sure there is a better way to do this, please post it if you find a way.
        for Action in Player.ActionList:
            if index == random:
                Player.PerformAction(Action, CurrentEnemy)
            index += 1
        #And now I do the same thing for the enemy.
        random = randint(0, len(CurrentEnemy.ActionList.keys())-1)
        index = 0
        for Action in CurrentEnemy.ActionList:
            if index == random:
                CurrentEnemy.PerformAction(Action, Player)
            index += 1
