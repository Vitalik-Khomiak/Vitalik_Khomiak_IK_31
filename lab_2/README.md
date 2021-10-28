# Vitalik_Khomiak_IK_31
    #Labs_2


1. Створив папку lab_2 з README.md файлом.
2. За допомогою пакетного менеджера PIP інсталював pipenv та створив ізольоване середовище для Python. Ознайомився з командаю pipenv -h.

    pip install pipenv
    pipenv --python 3.7
    pipenv shell

3. Встановив бібліотеку requests. Також встановив бібліотеку ntplib яка працює з часом.

    pipenv install requests
    pipenv install ntplib


4. Створив файл app.py. 
5. Переконався що програма працює правильно.

  Результат: 
  
    python app.py

    ========================================
    Результат без параметрів: 
    No URL passed to function
    ========================================
    Результат з правильною URL: 
    Time is:  01:26:38 PM
    Date is:  10-28-2021
    success


6. Встановив бібліотеку pytest.

    pipenv install pytest



