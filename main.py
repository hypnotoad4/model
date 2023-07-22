from collections import Counter

class player:
    def __init__(self,model):
        self.model = model
        self.history = []
class Mirror(player):
    def __init__(self,model):
        super().__init__(model)
        self.matches = 0
    def step(self):
        self.matches += 1
        if not self.history: return True
        elif self.history[-1]==True and self.matches%2==0: return False
        elif self.history[-1]==True and self.matches%2!=0: return True
        elif self.history[-1]==False and self.matches%2==0: return True
        elif self.history[-1]==False and self.matches%2!=0: return False



class Copycat(player):
    def step(self):
        return True if not self.history else self.history[-1]


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

g = Game(matches=10)

g.play(Mirror("Mirror"),Copycat("Copycat"))

for i in g.registry:
    print(i,g.registry[i])