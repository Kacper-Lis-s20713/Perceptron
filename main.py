import numpy as np


def prepare_data():
    with open('lang/english/1.txt', 'r', encoding="utf-8") as file:
        data = file.read().replace('\n', ' ')
        data = data.upper()
        letters = np.zeros(26)
        print(letters)
        for l in data:
            temp = ord(l)
            if temp>=65 and temp<=90:
                letters[temp-65] += 1
        print(letters)





if __name__ == '__main__':
    prepare_data()

