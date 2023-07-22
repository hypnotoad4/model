from collections import Counter

class player:
    def __init__(self,model):
        self.model = model
        self.history = []


class Mirror(player):
    def __init__(self,model):
        super().__init__(model)
        self.matches = 0 # счетчик матчей
    def step(self):
        #self.matches += 1 # можно раскомментить и закомментить счётчик вконце, чтобы посмотреть на другой результат 
        if not self.history: return True
        elif self.history[-1]==True and self.matches%2==0: return False
        elif self.history[-1]==True and self.matches%2!=0: return True
        elif self.history[-1]==False and self.matches%2==0: return True
        elif self.history[-1]==False and self.matches%2!=0: return False
        self.matches += 1



class Copycat(player):
    def step(self):
        return True if not self.history else self.history[-1]
    
class Cheater(player):
    def step(self):
        return False

class Cooperator(player):
    def step(self):
        return True


class Game(object):

    def __init__(self, matches=1000):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        for _ in range(self.matches):
            ans1,ans2 = player1.step(),player2.step()
            if ans1 and ans2:
                self.registry[player1.model]+=2
                self.registry[player2.model]+=2
            elif not ans1 and ans2:
                self.registry[player1.model]+=3
                self.registry[player2.model]-=1
            elif not ans2 and ans1:
                self.registry[player2.model]+=3
                self.registry[player1.model]-=1

            player2.history.append(ans1)
            player1.history.append(ans2)

        player2.history = []
        player1.history = []

g1 = Game(matches=1000)
g1.play(Mirror("Mirror"),Copycat("Вражина"))
for i in g1.registry: print(i,g1.registry[i])

g2 = Game(matches=1000)
g2.play(Mirror("Mirror"),Cheater("Вражина"))
for i in g2.registry: print(i,g2.registry[i])

g3 = Game(matches=1000)
g3.play(Mirror("Mirror"),Cooperator("Вражина"))
for i in g3.registry: print(i,g3.registry[i])