

class DayFourSolution():

    pairs = []

    counter = 0

    def __init__(self, file) -> None:

        with open(file) as f:

            aa = [x.split(",") for x in f.read().split()]

            for i in aa:
                j = [int(x) for x in i[0].split("-")]
                h = [int(x) for x in i[1].split("-")]

                x = set(range(j[0], j[1] + 1))
                y = set(range(h[0], h[1] + 1))

                if x.issubset(y) or set(y).issubset(x):
                    self.counter += 1

    def getPairs(self):
        return self.counter


aa = DayFourSolution("input.txt")

print(aa.getPairs())
