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
    
    def throw(self):
        throw = (random.randint(0,6), random.randint(0, 6))
        self.position += sum(throw)
        if throw[0] == throw[1]:
            return True
        else:
            return False
    

player1 = Player('0')
player2 = Player('1')
meme = 'memes'