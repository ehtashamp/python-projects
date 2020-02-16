"""
world cup class to add custom methods.
Overriding special functions based on their feature of the class 
and the process we wnat ot perform with the object data
"""
class wordCup(object):
    def __init__(self, name, *players):
        self.team_name = name
        self.players = players

    def __str__(self):
        return self.team_name
    
    def __len__(self):
        return (len(self.players))

    def __gt__(self,other):
        return True if (len(self.players) > len(other.players)) else False
    
    def __add__(self, other):
        return list(self.players + other.players)

india = wordCup('India', 'dhoni','virat', 'Sharma', 'kapil', 'raju')
australia = wordCup('Australia', 'Lee','Law', 'lim', 'tim')
#india points to self and australia points to others 
print(india + australia) #invoking __add__ special function by overriding the default functionlity 
print(india)
print(len(india), australia)
print(india > australia)
