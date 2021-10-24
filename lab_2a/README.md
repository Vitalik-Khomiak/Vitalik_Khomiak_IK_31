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

a. ---
Після запуску команди: python . -h в консоль виводиться інформація про додаткові параметри та їх використання. Результат виконання команди:

```python
E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python . -h
usage: . [-h] [-o OPT] [-l]
```

Приклад передачі аргументів у Python програму.

optional arguments:
  -h, --help            show this help message and exit
  -o OPT, --optional OPT
                        Цей параметр є вибірковим.
  -l, --logs            Якщо виконати команду з цим параметром будуть виводитись логи.

b. ---
Після запуску команди: python . -o "Цей текст також має вивестись" в консоль виводиться інформація така сама як і в пункті 2. тільки додається текст про те що з консолї було передано аргумент і саме повідомлення яке ми передаємо. Результат виконання команди:

```python
E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python . -o "Цей текст також має вивестись"
We are in the __main__
2021-10-23 22:09:12.396571
win32
З консолі було передано аргумент
 ========== >> Цей текст також має вивестись << ==========
test
```

c. ---
Детально ознайомився з аргументами. d. Ознайомився з логуванням і запустив команду python . --logs Результат виконання команди:

```python
E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python . --logs
2021-10-23 22:15:04,855 root INFO: Тут буде просто інформативне повідомлення
2021-10-23 22:15:04,856 root WARNING: Це Warning повідомлення
2021-10-23 22:15:04,857 root ERROR: Це повідомлення про помилку
test
```

Створив власну функцію у файлі common.py яка буде виводить всі парні числа від 0 до 100, якщо у функцію передати значення True і непарні якщо значення False. Виклик цієї функцію виконую з __main__ . Код власної функції:

```python
def filter(filter):
    numbers=range(0,101)
    if filter=="True":
    	msg = "paired elements: " 
    elif filter=="False":
    	msg = "odd elements: "
    
    for index in range(0, len(numbers)):
    	if (filter == "True") & (numbers[index]%2 == 0):
    	    msg += str(numbers[index]) + " "
    	elif (filter == "False") & (numbers[index]%2 != 0):
    	    msg += str(numbers[index]) + " "
    return msg

```
Результат виконання з параметром -o True:

```python
E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python . -o True
We are in the __main__
2021-10-24 09:41:19.540213
win32
Парні елементи: 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100
З консолі було передано аргумент
 ========== >> True << ==========
test
```

Результат виконання з параметром -o False:

```python
E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python . -o False
We are in the __main__
2021-10-24 09:40:57.135856
win32
Непарні елементи: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99
З консолі було передано аргумент
 ========== >> False << ==========
test
```




4. Створив функцію яка може виконуватись з помилкою. У випадку її виникнення виводить ERROR повідомлення за допомогою логування використовуючи бібліотеку logging. Якщо функція виконалася без помилки то виводить INFO повідомлення. Код власної функції:
```python
def s_arr():
    y = 200
    z = 11
    x=[random.randint(1, y)
       for i in range(z)]      
    print("arrray X[]:", x)
    index = int(input("Press element num: "))
    try:
    	print(f"X[{index}] = {x[index]}")
    	print('------------------------------------')
    except IndexError:
        logging.error("Num must be in range 0-%s", z-1)
    else:
    	logging.info("\nNice \n-_- -_- -_-")

```
Результат виконання з помилкою:
```python
E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python .
We are in the __main__
2021-10-24 09:59:53.222404
win32
arrray X[]: [92, 143, 29, 44, 147, 69, 25, 123, 102, 77, 126]
Press element num: 15
2021-10-24 09:59:56,143 root ERROR: Num must be in range 0-10
test

E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>
```

Результат виконання без помилки:
```python
E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>python .
We are in the __main__
2021-10-24 10:00:34.382228
win32
arrray X[]: [63, 92, 107, 101, 67, 58, 133, 65, 99, 44, 107]
Press element num: 10
X[10] = 107
------------------------------------
2021-10-24 10:00:36,303 root INFO:
Nice
-_- -_- -_-
test

E:\Google_Drive      (lol22725@gmail.com) (not syncing)\University\TPIS_git\Vitalik_Khomiak_IK_31\lab_2a>

```