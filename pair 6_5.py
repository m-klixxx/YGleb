import warnings
import math

ch1 = int(input("введіть 1 число: "))
ch2 = int(input("введіть 2 число: "))
ch3 = int(input("введіть 3 число: "))

def check(ch1,ch2,ch3):
    if ch1 % 5 == 0 and ch2 % 5 == 0 and ch3 % 5 == 0:
        sp=[ch1, ch2, ch3]
        sp.sort()
        print(sp)

    else:
      raise TypeError("Ви написали одне або декілька чисел які не діляться на 5!")


try:
    check(ch1, ch2, ch3)
except TypeError:
    print("Ви написали одне або декілька чисел які не діляться на 5!")