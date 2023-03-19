import sys
import math

# sprawdzenie czy podana ilosc argumentow jest prawidlowa i zapisanie ich zawartosci do zmiennych


if len(sys.argv) != 3:
    print('nieprawidlowa ilosc argumentow')
    raise TypeError(f"nieprawidlowa ilosc argumentow\nwymagane: 3\notrzymane: {len(sys.argv)}")

k = int(sys.argv[1])
trainSet = sys.argv[2]
testSet = sys.argv[3]

# utowrzenie klasy iris, na podstawie ktorej beda tworzenie obiekty opisujace te kwiaty


class Iris:

    def settype(self, n_type):
        self.v_type = n_type

    def __init__(self, a, b, c, d, v_type, distance):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.v_type = v_type
        self.distance = distance

# sortowanie podanej linii z pliku i zapisywnie jej zawartosci do obiektu


def sortline(v_line):
    info = v_line.split(",")
    a, b, c, d = info[0], info[1], info[2], info[3]
    if len(info) > 4:
        e = info[4]
        infoparts = e.split("-")
        n_type = infoparts[1]
        iris1 = Iris(a, b, c, d, n_type, 0)
    else:
        iris1 = Iris(a, b, c, d, 'D', 0)
    return iris1

# odczytywanie pliku i zapisywanie jego zawartosci do tablicy


def readfile(path):
    arr = list()
    with open(path, 'r') as text:
        for line in text:
            arr.append(sortline(line))
    return arr


# obliczanie odleglosci miedzy dwoma wektorami


def calculate(iris1, iris2):
    length = math.sqrt(math.pow(iris1.a - iris2.a, 2) + math.pow(iris1.b - iris2.b, 2)
                       + math.pow(iris1.c - iris2.c, 2) + math.pow(iris1.d - iris2.d, 2))
    return length

# funkcja znajdujaca najwieksza z 3 podanych liczb


def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# klasyfikacja irysow


def differentiation(iris1, trainlist):
    for i in trainlist:
        if i.v_type == 'D':
            i.distance = calculate(iris1, i)
    sortedlist = sorted(trainlist, key=lambda iris: iris.distance)
    klist = list()
    for i in range(0, k):
        klist.append(sortedlist[i])
    seto, ver, vir = 0, 0, 0
    for i in klist:
        if i.v_type == 'setosa':
            seto = seto+1
        elif i.v_type == 'versicolor':
            ver = ver+1
        elif i.v_type == "virginica":
            vir = vir+1
        else:
            print('type cannot be resolved')
    if max_of_three(seto, ver, vir) == seto:
        iris1.settype('setosa')
    elif max_of_three(seto, ver, vir) == ver:
        iris1.settype('versicolor')
    elif max_of_three(seto, ver, vir) == vir:
        iris1.settype('virginica')
    else:
        raise TypeError('could not find max of three')
    print(f"[{iris1.a}, {iris1.b}, {iris1.c}, {iris1.d}]\t{iris1.v_type}")


# otwieranie plików i zapisywanie ich zawartosci do tablic

train = readfile(trainSet)
test = readfile(testSet)
