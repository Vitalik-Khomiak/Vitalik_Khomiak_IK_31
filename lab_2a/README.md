# Vitalik_Khomiak_IK_31
Labs_2

1. Переглянув офіційну документацію для Python.

2.1 Створюю файл test.py для виконання базових прикладів.
Виводжу вбудованні константи за допомогою команд:
```python
print("First_constant: ", False)
print("Second_constant: ", None)	
print("Third_constant: ", True)
 ```
2.2 Виводжу результат роботи вбудованих функцій за допомогою команд:
```python
x = 2
print(f"x + 2 = {eval('x+2')}")
print(f"4 в квадраті = {pow(4,2)}")
print("Максимальне число з чисел 5,8,9,3,45 :",max(5,8,9,3,45))
```
2.3 Виводжу результат роботи розгалуження та циклу за допомогою команд:
```python
#a
x=10
if x==10:
    print ('x=10')

else:
    print ('x!=10')

#b
for x in "ArtLab":
  print(x)
7:36 PM 10/23/2021
```

2.4 Виводжу результат роботи конструкції try->except->finally при помилці за допомогою команд:
```python
x = '5'
try:
    x += 7
except TypeError as error:
    print(f"Error: {error}, occured !!!check your code")
finally:
    print("x = {x}({type(x)})")
```

2.5 Виводжу результат роботи контекст-менеджера with за допомогою команд:
```python
with open("1.txt", 'r') as readme_file:
    first_str = readme_file.readline()
    print(first_str)
```

2.6 Виводжу результат роботи з lambdas за допомогою команд:
```python
aor = lambda x, y: print(f"Площа: {x*y}")
aor(8,5)
```



3. Створив у власному рипозеторії такі файли:
```python
lab2a/
├── modules/
│   └── common.py
├── __init__.py
└── __main__.py
```

