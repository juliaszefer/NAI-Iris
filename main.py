import sys
import math

# sprawdzenie czy podana ilosc argumentow jest prawidlowa i zapisanie ich zawartosci do zmiennych


if len(sys.argv) != 3:
    print('nieprawidlowa ilosc argumentow')
    raise TypeError(f"nieprawidlowa ilosc argumentow\nwymagane: 3\notrzymane: {len(sys.argv)}")

k = sys.argv[1]
trainSet = sys.argv[2]
testSet = sys.argv[3]

# utowrzenie klasy iris, na podstawie ktorej beda tworzenie obiekty opisujace te kwiaty


class Iris:
    def __init__(self, a, b, c, d, v_type):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.v_type = v_type

# sortowanie podanej linii z pliku i zapisywnie jej zawartosci do obiektu


def sortline(v_line):
    info = v_line.split(",")
    a, b, c, d = info[0], info[1], info[2], info[3]
    if len(info) > 4:
        e = info[4]
        infoparts = e.split("-")
        n_type = infoparts[1]
        iris1 = Iris(a, b, c, d, n_type)
    else:
        iris1 = Iris(a, b, c, d, "")
    return iris1

# odczytywanie pliku i zapisywanie jego zawartosci do tablicy


def readfile(path):
    arr = []
    with open(path, 'r') as text:
        for line in text:
            arr.append(sortline(line))
    return arr


# obliczanie odleglosci miedzy dwoma wektorami


def calculate(iris1, iris2):
    length = math.sqrt(math.pow(iris1.a - iris2.a, 2) + math.pow(iris1.b - iris2.b, 2)
                       + math.pow(iris1.c - iris2.c, 2) + math.pow(iris1.d - iris2.d, 2))
    return length


# otwieranie plików i zapisywanie ich zawartosci do tablic

train = readfile(trainSet)
test = readfile(testSet)
