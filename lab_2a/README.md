# Vitalik_Khomiak_IK_31
Labs_2a

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

3.1 Перейшовши у папку з даними файлами запустив виконання програми цією командою:
```python
python .
```

Виконання команди:
```python
E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python .
We are in the __main__
2021-10-23 21:58:43.005686
win32
test
```
3.2 Після запуску команди python . програма в першому рядку виводить назву файла який виконувався, в другому рядку виводиться час і дата виконання даної програми, в третьому рядку виводиться ос на якій було запущено програму і в четвертому рядку виведено текст "test".

a. Після запуску команди: python . -h в консоль виводиться інформація про додаткові параметри та їх використання. Результат виконання команди:

E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python . -h
usage: . [-h] [-o OPT] [-l]

Приклад передачі аргументів у Python програму.

optional arguments:
  -h, --help            show this help message and exit
  -o OPT, --optional OPT
                        Цей параметр є вибірковим.
  -l, --logs            Якщо виконати команду з цим параметром будуть виводитись логи.

b. Після запуску команди: python . -o "Цей текст також має вивестись" в консоль виводиться інформація така сама як і в пункті 2. тільки додається текст про те що з консолї було передано аргумент і саме повідомлення яке ми передаємо. Результат виконання команди:

E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python . -o "Цей текст також має вивестись"
We are in the __main__
2021-10-23 22:09:12.396571
win32
З консолі було передано аргумент
 ========== >> Цей текст також має вивестись << ==========
test

c. Детально ознайомився з аргументами. d. Ознайомився з логуванням і запустив команду python . --logs Результат виконання команди:

E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python . --logs
2021-10-23 22:15:04,855 root INFO: Тут буде просто інформативне повідомлення
2021-10-23 22:15:04,856 root WARNING: Це Warning повідомлення
2021-10-23 22:15:04,857 root ERROR: Це повідомлення про помилку
test

Створив власну функцію у файлі common.py яка буде виводить всі парні числа від 0 до 100, якщо у функцію передати значення True і непарні якщо значення False. Виклик цієї функцію виконую з __main__ . Код власної функції:

```python
def filter (filter):
    num=range(0,101)
    if filter=="True":
        m = "even numbers: " 
    elif filter=="False":
        m = "odd numbers: "

    for index in num:
        if (filter == "True") & (num[index]%2 == 0):
            m += str(num[index]) + " "
        elif (filter == "False") & (num[index]%2 != 0):
            m += str(num[index]) + " "
    return m

```
Результат виконання з параметром -o True:

```python
E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python . -o True
We are in the __main__
2021-10-23 22:35:25.215600
win32
З консолі було передано аргумент
 ========== >> True << ==========
test
```

Результат виконання з параметром -o False:

```python
E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python . -o False
We are in the __main__
2021-10-23 22:36:15.417472
win32
З консолі було передано аргумент
 ========== >> False << ==========
test
```
