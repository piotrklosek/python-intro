# Importowanie modułu math (https://docs.python.org/3/library/math.html)
import math 

# Tworzenie dwóch list
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# Łączenie list za pomocą funkcji zip() (https://docs.python.org/3/library/functions.html#zip)
zipped_lists = list(zip(list1, list2))
print("Połączone listy:", zipped_lists)

# Przykład funkcji z modułu math
try:
    number = -25
    result = math.sqrt(number)  # Próba obliczenia pierwiastka kwadratowego z liczby ujemnej
except ValueError as e:
    print("\nBłąd: Nie można obliczyć pierwiastka kwadratowego z liczby ujemnej :",number)
    print("Szczegóły błędu:", e)
