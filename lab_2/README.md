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

7. Tests:

    (lab_2) sh-5.1$ pytest tests/tests.py
    ========================================================================== test session starts      
    platform linux -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
    rootdir: /home/artlab/Desktop/rep/lab_2
    collected 5 items                                                                                                                                                        

    tests/tests.py .....                                                                                                                                               [100%]

    =========================================================================== 5 passed in 0.92s 
 
8. ❗ (Захист) У програмі дописав функцію яка буде перевіряти час доби AM/PM та відповідно друкувати: Good day/night.

    Код програми:
    
    ef home_work(t=datetime.today().strftime("%H:%M %p")):
    # Ваш захист
    if 'PM' in t:
        print ("Good night")
        return 'Good night'
    if 'AM' in t:
        print ("Good day")
        return 'Good day'




    Запуск програми:
    
    (lab_2) artlab@artlab-VirtualBox:~/Desktop/rep/lab_2$ python app.py
    ========================================
    Результат без параметрів: 
    Good day
    No URL passed to function
    ========================================
    Результат з правильною URL: 
    Good day
    Time is:  08:52:47 AM
    Date is:  10-29-2021
    (lab_2) artlab@artlab-VirtualBox:~/Desktop/rep/lab_2$ 


9. ❗ (Захист) Написав тест що буде перевіряти правильність виконання моєї функції.


    Код програми:
    
    def test_home_work(self):
    # Ваш захист
    self.assertEqual(home_work("20:20:20 PM"), "Good night")
    self.assertEqual(home_work("10:10:10 AM"), "Good day")


    Запуск програми:
    
    (lab_2) artlab@artlab-VirtualBox:~/Desktop/rep/lab_2$ pytest tests/tests.py
    ============================= test session starts 
    platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
    rootdir: /home/artlab/Desktop/rep/lab_2
    collected 5   
    items                                                              

    tests/tests.py .....   
    [100%]

    ============================== 5 passed in 1.00s 



