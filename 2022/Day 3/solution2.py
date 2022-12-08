import string


class DayThreeSolution():

    racksacks = []
    priorities = dict(zip(list(string.ascii_letters), range(1, 53)))

    points = 0

    def __init__(self, file) -> None:

        with open(file) as f:
            a = f.read().split()

            def slice(l, n):

                for i in range(0, len(l), n):
                    yield l[i:i + n]

            bb = list(slice(a, 3))

        for i in bb:
            x = ''.join((set(x for x in i[0] if x in i[1] and x in i[2])))

            self. points += self.priorities.get(x)

    def getList(self):
        return self.points


aa = DayThreeSolution('input.txt')
print(aa.getList())
