def lower_up(lower, upper):
    """ 1: Returns a list of numbers from the lower number to the upper number:
    >>> lower_up(5,15)
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    """
    for n in range(lower, upper + 1):
        print(n)


def all_the_args(*args, **kwargs):
    """ 2: Return an array. Use * to expand positional args
    and use ** to expand keyword args

    >>> all_the_args(1, 2, a=3, b=4)
    (1, 2)
    {'a': 3, 'b': 4}
    """
    print args
    print kwargs


def may_20(tup):
    """ 3: Definir una tupla con 10 numeros. Imprimir la
    cantidad de numeros superiores a 20.
    >>> may_20([10, 16, 22, 26, 27, 30])
    22, 26, 27, 30

    """
    string = ""
    for n in filter(lambda x: x > 20, tup):
        string += str(n) + ", "
    print string[:len(string) - 2]


def word_filter(list_of_words, n):
    """ 4: Filtra las palabras que contienen mas de n caracteres.

    >>> word_filter(["hello", "bye", "computer", "software", "python"], 5)
    ['computer', 'software', 'python']

    """
    return filter(lambda x: len(x) > n, list_of_words)


def string_length(list):
    """ 5: imprime el largo de una cadena de caracteres

    >>> string_length("popularity")
    10
    """
    return len(list)


def is_vocal(x):
    """ 6: Determines if it is vocal

    >>> is_vocal("a")
    True
    >>> is_vocal("b")
    False
    """
    return x in ("a", "e", "i", "o", "u")


def is_leap_year(year):
    """ 7: Determines if a year is a leap year.

    >>> is_leap_year(2016)
    True
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def has_uppercase(word):
    """ 8: Evaluate if a word has uppercase letters

    >>> has_uppercase("MayuSculA")
    3
    """
    return len(filter(lambda x: x.isupper(), word))


def contar_vocales(cadena):
    """ 9: Return number of vocales in a word.

    >>> contar_vocales("murcielago")
    5
    """
    return len(filter(lambda x: x in ("a", "e", "i", "o", "u"),  cadena))


def square(list):
    """ 10: Calculate the square of the numbers in a list

    >>> l = [0, 1, 2, 3]
    >>> square(l)
    [0, 1, 4, 9]
    """
    return map(lambda x: x**2, list)


def is_prime(n):
    """ 11:  Return if n is prime.

    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    return all(n % i for i in xrange(2, n))


def factorial(n):
    """ 12: Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(long(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000L
    """
    return int(1 if (n < 1) else n * factorial(n - 1))


def to_roman(n):
    """ 13: Convert number integer to Roman numeral

    >>> to_roman(598)
    'DXCVIII'
    """
    val = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    syb = ('M',  'CM', 'D', 'CD', 'C', 'XC',
           'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    roman_num = ""
    for i in range(len(val)):
        count = int(n / val[i])
        roman_num += syb[i] * count
        n -= val[i] * count
    return roman_num


def rima(word1, word2):
    """ 14: Indica si dos palabrar riman. Si coinciden las 3 ultimas letras rima,
        si ncoinciden solo 2 rima un poco, si coincide solo 1 no rima.

    >>> rima("flor", "coliflor")
    'rima'
    >>> rima("amar", "plantar")
    'rima un poco.'
    >>> rima("azucar", "barrer")
    'no rima'
    """
    res = list()
    res.append("no rima")
    res.append("rima un poco.")
    res.append("rima")
    return res[coinsidencia(word1, word2) - 2]


def capital(pesos, interes, anios):
    """ 15: Pide una cantidad de pesos, una tasa de interes y
    un numero de anios. Muestra en cuanto se habra convertido el
    capital inicial transcurridos esos anios si cada anio se aplica
    la tasa de interes introducida.

    >>> capital(10000, 4.5, 20)
    24117.14
    """
    return float("%.2f" % (pesos * (1 + interes / 100)**anios))


def coinsidencia(pal1, pal2):
    con = 1
    while pal1[::-1][:con] == pal2[::-1][:con]:
        con += 1
    return pack(con)


def pack(num):
    if num > 4:
        return 4
    return num
