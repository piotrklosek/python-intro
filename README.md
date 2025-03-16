# Dokumentacja wybranych zagadnień języka Python

## Funkcja wbudowana: `zip()`
Funkcja `zip()` służy do łączenia elementów z dwóch lub więcej iterowalnych obiektów w krotki. Zwraca iterator, którego elementy to krotki zawierające odpowiadające sobie elementy z podanych iterowalnych obiektów.

### Przykład użycia:
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(zipped)  # [(1, 'a'), (2, 'b'), (3, 'c')]
```
📌 [Dokumentacja `zip()`](https://docs.python.org/3/library/functions.html#zip)

---

## Funkcja wbudowana: `enumerate()`
Funkcja `enumerate()` dodaje licznik do iterowalnego obiektu, zwracając pary `(indeks, wartość)`.

### Przykład użycia:
```python
items = ['apple', 'banana', 'cherry']
for index, value in enumerate(items):
    print(index, value)
```
📌 [Dokumentacja `enumerate()`](https://docs.python.org/3/library/functions.html#enumerate)

---

## Funkcja wbudowana: `sorted()`
Funkcja `sorted()` zwraca nową posortowaną listę na podstawie przekazanego iterowalnego obiektu.

### Przykład użycia:
```python
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 3, 4, 5, 9]
```
📌 [Dokumentacja `sorted()`](https://docs.python.org/3/library/functions.html#sorted)

---

## Moduł standardowy: `math`
Moduł `math` zawiera funkcje matematyczne, takie jak pierwiastkowanie, funkcje trygonometryczne, stałe matematyczne (`pi`, `e`), zaokrąglanie i operacje na liczbach.

### Przykład użycia:
```python
import math
print(math.sqrt(16))  # 4.0
print(math.sin(math.pi / 2))  # 1.0
```
📌 [Dokumentacja `math`](https://docs.python.org/3/library/math.html)

---

## Moduł standardowy: `random`
Moduł `random` pozwala generować liczby losowe i wykonywać operacje losowe na zbiorach danych.

### Przykład użycia:
```python
import random
print(random.randint(1, 10))  # Losowa liczba całkowita z zakresu 1-10
print(random.choice(['apple', 'banana', 'cherry']))  # Losowy wybór z listy
```
📌 [Dokumentacja `random`](https://docs.python.org/3/library/random.html)

---

## Moduł standardowy: `time`
Moduł `time` pozwala na operacje związane z czasem, np. pobieranie aktualnego czasu, opóźnienia itp.

### Przykład użycia:
```python
import time
print("Start")
time.sleep(2)  # Pauza na 2 sekundy
print("Koniec")
```
📌 [Dokumentacja `time`](https://docs.python.org/3/library/time.html)

---

## Wyjątek: `ValueError`
`ValueError` występuje, gdy funkcja otrzymuje poprawny typ danych, ale wartość jest nieodpowiednia do wykonania danej operacji.

### Przykład użycia:
```python
try:
    number = int("abc")  # Próba konwersji niepoprawnego ciągu znaków na liczbę
except ValueError as e:
    print("Błąd:", e)
```
📌 [Dokumentacja `ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)

---

## Wyjątek: `ZeroDivisionError`
`ZeroDivisionError` występuje, gdy próbujemy podzielić liczbę przez zero.

### Przykład użycia:
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Błąd:", e)
```
📌 [Dokumentacja `ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError)
