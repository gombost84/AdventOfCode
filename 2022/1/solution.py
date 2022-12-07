

class Elves():

    listOfCalories = []
    listOfSums = []
    firstCal = 0
    secondCal = 0
    thirdCal = 0

    def __init__(self, file) -> None:
        
        with open(file, 'r') as f:
            a = f.read().split('\n\n')
            
            for i in a:
                self.listOfCalories.append(i.split())

    def getList(self):

        for i in self.listOfCalories:
            self.listOfSums.append(sum([int(x) for x in i]))
        
        self.listOfSums.sort()

        self.firstCal = self.listOfSums[-1]
        self.secondCal = self.listOfSums[-2]
        self.thirdCal = self.listOfSums[-3]

        return self.firstCal + self.secondCal + self.thirdCal

aa = Elves("input.txt")

print(aa.getList())