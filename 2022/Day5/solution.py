import pandas as pd
import csv


class DayFiveSolution():

    def __init__(self, file) -> None:

        with open(file, newline='') as f:
            aa = f.read().split('\r\n\r')
            bb = aa[0]

            bb = pd.DataFrame(bb.splitlines())
            bb.explode([0])

            print(bb)


aa = DayFiveSolution("input.txt")
