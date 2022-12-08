

class DayTwoSolution():

    matchList = []
    points = 0

    outcomes = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6
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
