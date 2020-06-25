from car_class import Car
from mexp import *

if __name__ == "__main__":
    listTesti = []
    listTesti.append(Car('Jack', 'benlalla', True, 1))
    listTesti.append(Car('Jack2', 'elarrs', False, 5))
    listTesti.append(Car('Marc', 'roro', False, 2))
    result = find(listTesti, lname = 'roro')
    print(result)