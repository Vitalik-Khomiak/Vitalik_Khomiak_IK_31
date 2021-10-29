# Vitalik_Khomiak_IK_31
    #Labs_2


1. Створив папку lab_2 з README.md файлом.
2. За допомогою пакетного менеджера PIP інсталював pipenv та створив ізольоване середовище для Python. Ознайомився з командаю pipenv -h.
```text
    pip install pipenv
    pipenv --python 3.7
    pipenv shell
```

3. Встановив бібліотеку requests. Також встановив бібліотеку ntplib яка працює з часом.
```text
    pipenv install requests
    pipenv install ntplib
```

4. Створив файл app.py. 
5. Переконався що програма працює правильно.
```text
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

```
6. Встановив бібліотеку pytest.
```text
    pipenv install pytest
```
7. Tests:
```
    (lab_2) sh-5.1$ pytest tests/tests.py
    ========================================================================== test session starts      
    platform linux -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
    rootdir: /home/artlab/Desktop/rep/lab_2
    collected 5 items                                                                                                                                                        

    tests/tests.py .....                                                                                                                                               [100%]

    =========================================================================== 5 passed in 0.92s 
```
8. ❗ (Захист) У програмі дописав функцію яка буде перевіряти час доби AM/PM та відповідно друкувати: Good day/night.
```text
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
```

9. ❗ (Захист) Написав тест що буде перевіряти правильність виконання моєї функції.

```text
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
```

10. Перенаправляю результат виконання тестів у файл ***results.txt*** за допомогою команди
```text
pytest tests/tests.py > results.txt
```
а також додаю результат виконання програми у кінець цього ж файл за допомогою команди 
```text
python app.py >> results.txt
```

11. Зробив коміт із змінами до свого репозиторію.

12. Заповнив ***Makefile*** необхідними командами (bash) для повної автоматизації процесу СІ мого проекту:
Вміст ***Makefile***:
```text




```
13. Закомітив зміни в Makefile до власного репозиторію.

14. Склонував *git* репозиторій на віртуальну машину Ubuntu. Перейшов у папку з  лабораторною роботою та запустив *Makefile*
файл за допомогти команди 

```text
make add
```


Результатом виконання цієї команди є створено ізольоване середовище, виконано тести, запущено програму та закомічено файл у git репозеторій.

```text
    (lab_2) artlab@artlab-VirtualBox:~/Desktop/rep/lab_2$ make all
    -----------A---r---t---L---A---B-----------
    Installing pipenv and dependencies.
    -----------A---r---t---L---A---B-----------
    sudo pip install pipenv
    Requirement already satisfied: pipenv in /usr/local/lib/python3.8/dist-packages (2021.5.29)
    Requirement already satisfied: virtualenv-clone>=0.2.5 in /usr/local/lib/python3.8/dist-packages (from pipenv) (0.5.7)
    Requirement already satisfied: certifi in /usr/lib/python3/dist-packages (from pipenv) (2019.11.28)
    Requirement already satisfied: setuptools>=36.2.1 in /usr/lib/python3/dist-packages (from pipenv) (45.2.0)
    Requirement already satisfied: virtualenv in /usr/local/lib/python3.8/dist-packages (from pipenv) (20.9.0)
    Requirement already satisfied: pip>=18.0 in /usr/lib/python3/dist-packages (from pipenv) (20.0.2)
    Requirement already satisfied: backports.entry-points-selectable>=1.0.4 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (1.1.0)
    Requirement already satisfied: six<2,>=1.9.0 in /usr/lib/python3/dist-packages (from virtualenv->pipenv) (1.14.0)
    Requirement already satisfied: filelock<4,>=3.2 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (3.3.1)
    Requirement already satisfied: platformdirs<3,>=2 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (2.4.0)
    Requirement already satisfied: distlib<1,>=0.3.1 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (0.3.3)
    sudo pipenv --python 3.8
    Virtualenv already exists!
    Removing existing virtualenv...
    Creating a virtualenv for this project...
    Pipfile: /home/artlab/Desktop/rep/lab_2/Pipfile
    Using /usr/bin/python3.8 (3.8.10) to create virtualenv...
    ⠴ Creating virtual environment...created virtual environment CPython3.8.10.final.0-64 in 267ms
      creator CPython3Posix(dest=/root/.local/share/virtualenvs/lab_2-so4_wSds, clear=False, no_vcs_ignore=False, global=False)
      seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/root/.local/share/virtualenv)
        added seed packages: pip==21.3.1, setuptools==58.3.0, wheel==0.37.0
      activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

    ✔ Successfully created virtual environment! 
    Virtualenv location: /root/.local/share/virtualenvs/lab_2-so4_wSds
    sudo pipenv install requests
    Installing requests...
    Adding requests to Pipfile's [packages]...
    ✔ Installation Succeeded 
    Installing dependencies from Pipfile.lock (18d437)...
      🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 9/9 — 00:00:04
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.
    sudo pipenv install ntplib
    Installing ntplib...
    Adding ntplib to Pipfile's [packages]...
    ✔ Installation Succeeded 
    Installing dependencies from Pipfile.lock (18d437)...
      🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.
    sudo pipenv install pytest
    Installing pytest...
    Adding pytest to Pipfile's [packages]...
    ✔ Installation Succeeded 
    Installing dependencies from Pipfile.lock (18d437)...
      🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.
    -----------A---r---t---L---A---B-----------
    Start tests.
    -----------A---r---t---L---A---B-----------
    sudo pipenv run pytest tests/tests.py > results.txt
    -----------A---r---t---L---A---B-----------
    Running Python app.
    -----------A---r---t---L---A---B-----------
    sudo pipenv run python app.py >> results.txt
    -----------A---r---t---L---A---B-----------
    Adding and Committing results.txt to git.
    -----------A---r---t---L---A---B-----------
    git add results.txt
    git commit -m "Automatic commit by MakeFile"
    [main f20f789] Automatic commit by MakeFile
     2 files changed, 119 insertions(+), 2 deletions(-)
     create mode 100644 lab_2/README2.md
    git push
    Username for 'https://github.com': artlab
    Password for 'https://artlab@github.com': 
    remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
    remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
    fatal: Authentication failed for 'https://github.com/Vitalik-Khomiak/Vitalik_Khomiak_IK_31.git/'
    make: *** [Makefile:33: deploy] Error 128
    (lab_2) artlab@artlab-VirtualBox:~/Desktop/rep/lab_2$ make all
    -----------A---r---t---L---A---B-----------
    Installing pipenv and dependencies.
    -----------A---r---t---L---A---B-----------
    sudo pip install pipenv
    Requirement already satisfied: pipenv in /usr/local/lib/python3.8/dist-packages (2021.5.29)
    Requirement already satisfied: certifi in /usr/lib/python3/dist-packages (from pipenv) (2019.11.28)
    Requirement already satisfied: pip>=18.0 in /usr/lib/python3/dist-packages (from pipenv) (20.0.2)
    Requirement already satisfied: setuptools>=36.2.1 in /usr/lib/python3/dist-packages (from pipenv) (45.2.0)
    Requirement already satisfied: virtualenv-clone>=0.2.5 in /usr/local/lib/python3.8/dist-packages (from pipenv) (0.5.7)
    Requirement already satisfied: virtualenv in /usr/local/lib/python3.8/dist-packages (from pipenv) (20.9.0)
    Requirement already satisfied: backports.entry-points-selectable>=1.0.4 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (1.1.0)
    Requirement already satisfied: platformdirs<3,>=2 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (2.4.0)
    Requirement already satisfied: six<2,>=1.9.0 in /usr/lib/python3/dist-packages (from virtualenv->pipenv) (1.14.0)
    Requirement already satisfied: distlib<1,>=0.3.1 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (0.3.3)
    Requirement already satisfied: filelock<4,>=3.2 in /usr/local/lib/python3.8/dist-packages (from virtualenv->pipenv) (3.3.1)
    sudo pipenv --python 3.8
    Virtualenv already exists!
    Removing existing virtualenv...
    Creating a virtualenv for this project...
    Pipfile: /home/artlab/Desktop/rep/lab_2/Pipfile
    Using /usr/bin/python3.8 (3.8.10) to create virtualenv...
    ⠦ Creating virtual environment...created virtual environment CPython3.8.10.final.0-64 in 302ms
      creator CPython3Posix(dest=/root/.local/share/virtualenvs/lab_2-so4_wSds, clear=False, no_vcs_ignore=False, global=False)
      seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/root/.local/share/virtualenv)
        added seed packages: pip==21.3.1, setuptools==58.3.0, wheel==0.37.0
      activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

    ✔ Successfully created virtual environment! 
    Virtualenv location: /root/.local/share/virtualenvs/lab_2-so4_wSds
    sudo pipenv install requests
    Installing requests...
    Adding requests to Pipfile's [packages]...
    ✔ Installation Succeeded 
    Installing dependencies from Pipfile.lock (18d437)...
      🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 9/9 — 00:00:06
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.
    sudo pipenv install ntplib
    Installing ntplib...
    Adding ntplib to Pipfile's [packages]...
    ✔ Installation Succeeded 
    Installing dependencies from Pipfile.lock (18d437)...
      🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.
    sudo pipenv install pytest
    Installing pytest...
    Adding pytest to Pipfile's [packages]...
    ✔ Installation Succeeded 
    Installing dependencies from Pipfile.lock (18d437)...
      🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.
    -----------A---r---t---L---A---B-----------
    Start tests.
    -----------A---r---t---L---A---B-----------
    sudo pipenv run pytest tests/tests.py > results.txt
    -----------A---r---t---L---A---B-----------
    Running Python app.
    -----------A---r---t---L---A---B-----------
    sudo pipenv run python app.py >> results.txt
    -----------A---r---t---L---A---B-----------
    Adding and Committing results.txt to git.
    -----------A---r---t---L---A---B-----------
    git add results.txt
    git commit -m "Automatic commit by MakeFile"
    [main 636cb96] Automatic commit by MakeFile
     1 file changed, 2 insertions(+), 2 deletions(-)
    git push
    Username for 'https://github.com': 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
    Password for 'https://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@github.com': 
    Enumerating objects: 11, done.
    Counting objects: 100% (11/11), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (8/8), done.
    Writing objects: 100% (8/8), 757 bytes | 151.00 KiB/s, done.
    Total 8 (delta 6), reused 0 (delta 0)
    remote: Resolving deltas: 100% (6/6), completed with 3 local objects.
    To https://github.com/Vitalik-Khomiak/Vitalik_Khomiak_IK_31.git
       54e035b..636cb96  main -> main
    (lab_2) artlab@artlab-VirtualBox:~/Desktop/rep/lab_2$ 

```


