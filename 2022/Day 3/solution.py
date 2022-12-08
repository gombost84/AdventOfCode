import string


class DayThreeSolution():

    racksacks = []
    priorities = {}

    points = 0

    def __init__(self, file) -> None:

        self.priorities = dict(zip(list(string.ascii_letters), range(1, 53)))

        with open(file) as f:
            self.racksacks = [[x[0:int((len(x)/2))], x[int(len(x)/2):]] for x in f.read().split()]

        for i in self.racksacks:
            x = ''.join((set(x for x in i[0] if x in i[1])))

            self.points += self.priorities.get(x)

    def getList(self):
        return self.points


aa = DayThreeSolution('input.txt')

print(aa.getList())
