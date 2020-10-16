import random

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
        
    def pay(self, target, amount):
        self.money -= amount
        target.money += amount
        
    def placeData(self):
        res = next((sub for sub in monopolyData['tiles'] if sub['name'] == chance['tileid']), None) 
    
    def throw(self):
        throw = (random.randint(0,6), random.randint(0, 6))
        self.position += sum(throw)
        if throw[0] == throw[1]:
            return True
        else:
            return False
    
    @classmethod
    def makePlayers(cls, count):
        players = []
        for player in range(count):
            players.append(Player(str(player)))
        return players            
    

players = Player.makePlayers(4)

