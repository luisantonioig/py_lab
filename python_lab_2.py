from contracts import contract
from typing import Iterator

@contract(lower='int,>0', upper='int,>0')
def lower_up(lower: int, upper: int):
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

def all_the_args(*args: int, **kwargs: int):
    """ 2: Return an array. Use * to expand positional args
    and use ** to expand keyword args

    >>> all_the_args(1, 2, a=3, b=4)
    (1, 2)
    {'a': 3, 'b': 4}
    """
    print(args)
    print(kwargs)

@contract(tup='list[int]', returns='list[N]')
def may_20(tup: Iterator[int]):
    """ 3: Definir una tupla con 10 numeros. Imprimir la
    cantidad de numeros superiores a 20.
    >>> may_20([10, 16, 22, 26, 27, 30])
    [22, 26, 27, 30]

    """
    if tup == None:
        return list()
    return list(filter(lambda x: x > 20, tup))

@contract(n='int,>0', list_of_words='list[int]', returns='list[N]')
def word_filter(list_of_words: Iterator[str], n: int) -> Iterator[str]:
    """ 4: Filtra las palabras que contienen mas de n caracteres.

    >>> word_filter(["hello", "bye", "computer", "software", "python"], 5)
    ['computer', 'software', 'python']

    """
    return list(filter(lambda x: len(x) > n, list_of_words))

@contract(s='str', returns='int')
def string_length(s: str) -> int:
    """ 5: imprime el largo de una cadena de caracteres

    >>> string_length("popularity")
    10
    """
    return sum([1 for i in s])

@contract(x='str', returns='bool')
def is_vocal(x: str) -> bool:
    """ 6: Determines if it is vocal

    >>> is_vocal("a")
    True
    >>> is_vocal("b")
    False
    """
    return x in ("a", "e", "i", "o", "u")

@contract(year='int,>0', returns='bool')
def is_leap_year(year: int) -> bool:
    """ 7: Determines if a year is a leap year.

    >>> is_leap_year(2016)
    True
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

@contract(word='str', returns='int')
def has_uppercase(word: str) -> int:
    """ 8: Evaluate if a word has uppercase letters

    >>> has_uppercase("MayuSculA")
    3
    """
    return sum(1 for _ in filter(lambda x: x.isupper(), word))

@contract(cadena='str', returns='int')
def contar_vocales(cadena: str) -> int:
    """ 9: Return number of vocales in a word.

    >>> contar_vocales("murcielago")
    5
    """
    return sum(1 for _ in filter(lambda x: x in ("a", "e", "i", "o", "u"),  cadena))

@contract(cadena='str', returns='int')
def contar_consonantes(cadena: str) -> int:
    """ 9: Return number of vocales in a word.

    >>> contar_vocales("murcielago")
    5
    """
    return sum(1 for _ in filter(lambda x: x not in ("a", "e", "i", "o", "u"),  cadena))

@contract(l='list[int]', returns='list[int]')
def square(l: Iterator[int]) -> Iterator[int]:
    """ 10: Calculate the square of the numbers in a list

    >>> l = [0, 1, 2, 3]
    >>> square(l)
    [0, 1, 4, 9]
    """
    return list(map(lambda x: x**2, l))

@contract(n='int,>0', returns='bool')
def is_prime(n: int) -> bool:
    """ 11:  Return if n is prime.

    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    return all(n % i for i in range(2, n))

@contract(n='int')
def factorial(n: int) -> int:
    """ 12: Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    """
    return int(1 if (n < 1) else n * factorial(n - 1))

@contract(n='int,>0', returns='str')
def to_roman(n: int) -> str:
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

@contract(word1='str', word2='str', returns='str')
def rima(word1: str, word2: str) -> str:
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


@contract(pesos='int,>0', interes='float', anios='int', returns='float')
def capital(pesos: int, interes: float, anios: int) -> float:
    """ 15: Pide una cantidad de pesos, una tasa de interes y
    un numero de anios. Muestra en cuanto se habra convertido el
    capital inicial transcurridos esos anios si cada anio se aplica
    la tasa de interes introducida.

    >>> capital(10000, 4.5, 20)
    24117.14
    """
    return float("%.2f" % (pesos * (1 + interes / 100)**anios))


@contract(pal1='str', pal2='str', returns='int')
def coinsidencia(pal1: str, pal2:str) -> int:
    con = 1
    while pal1[::-1][:con] == pal2[::-1][:con]:
        con += 1
    return pack(con)

@contract(num='int,>0', returns='int')
def pack(num: int) -> int:
    if num > 4:
        return 4
    return num
