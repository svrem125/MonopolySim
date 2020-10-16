import random
import json

data = json.load(open('data.json'))

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
        # print(self.position)
        # res = next((sub for sub in data['properties'] if sub['position'] == self.position))
        # print(res)
        self.place = data['tiles'][self.position]
         
    
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
    

player1 = Player('1')
player2 = Player('2')
player3 = Player('3')
player4 = Player('4')

player2.throw()
player2.placeData()