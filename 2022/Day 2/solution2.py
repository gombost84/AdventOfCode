

class DayTwoSolution():

    matchList = []
    points = 0

    outcomes = {
        'A X': 3,
        'B X': 1,
        'C X': 2,
        'A Y': 4,
        'B Y': 5,
        'C Y': 6,
        'A Z': 8,
        'B Z': 9,
        'C Z': 7
    }

    def __init__(self, file) -> None:
        
        with open(file) as f:

            self.matchList = [x for x in f.read().split("\n")]

    
    def getPoints(self):
        
        for i in self.matchList:
            self.points += self.outcomes.get(i)

        return self.points


aa = DayTwoSolution("input.txt")

print(aa.getPoints())