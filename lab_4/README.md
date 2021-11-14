# Лабораторна робота №4
---

1. Для ознайомляння з Docker звернувся до документації.

2. Для перевірки чи докер встановлений і працює правильно на віртуальній машині запустітив перевірку версії командою 

```python
sudo docker -v > my_work.log 
```

виведення допомоги командою 

```text
sudo docker --help >> my_work.log 
```

та тестовий імедж командою 

```text
sudo docker run docker/whalesay cowsay Docker is fun >> my_work.log 
```

Вивід цих команд перенаправляв у файл my_work.log та закомітив його до репозиторію.

3. Як можна бачити Docker працює з Імеджами та Контейнерами. Імедж це свого роду операційна система з попередньо інстальованим ПЗ. Контейнер це запущений Імедж. Ідея роботи Docker дещо схожа на віртуальні машини. Перш за все потрібно створити імедж з якого буде запускатись контейнер. Для цього існує Dockerfile який описує контент імеджу. Ознайомтесь з документацією.

4. Для знайомства з Docker створив імедж із Django сайтом зробленим у попередній роботі.
    1) Оскільки мій проект на Python то і базовий імедж також потрібно вибрати відповідний. Всі імеджі можна знайти на [Python Docker Hub](https://hub.docker.com/_/python). Використав команду щоб завантажити базовий імедж з репозиторію: (_це можна і не робити, оскільки при запуску Dockerfile може самостійно його завантажити_)
    

```python
    docker pull python:3.8-slim
```


```python
artlab@artlab-VirtualBox:~/PycharmProjects/Vitalik_Khomiak_IK_31/lab_4$ sudo docker pull python:3.8-slim
3.8-slim: Pulling from library/python
7d63c13d9b9b: Pull complete 
7c9d54bd144b: Pull complete 
6c659176d5c8: Pull complete 
31bfadeaf52b: Pull complete 
2bb8ff279f62: Pull complete 
Digest: sha256:d31a1beb6ccddbf5b5c72904853f5c2c4d1f49bb8186b623db0b80f8c37b5899
Status: Downloaded newer image for python:3.8-slim
docker.io/library/python:3.8-slim

```


```python
    docker images
```

```python
artlab@artlab-VirtualBox:~/PycharmProjects/Vitalik_Khomiak_IK_31/lab_4$ sudo docker images
REPOSITORY        TAG        IMAGE ID       CREATED       SIZE
python            3.8-slim   214d62795dbb   2 weeks ago   122MB
docker/whalesay   latest     6b362a9f73eb   6 years ago   247MB
```

```python
    docker inspect python:3.7-slim
```

    2) Створив файл з іменем Dockerfile скопіював туди вмісt такого ж файлу з цього репозиторію;
    3) Ознайомився із коментарями та постарався зрозуміти структуру написання Dockerfile;
    4) Замінив посилання на власний Git репозиторій із моїм веб-сайтом та закомітив даний Dockerfile*

```python
FROM python:3.8-slim

LABEL author="Bohdan"
LABEL version=1.0

# оновлюємо систему
RUN apt-get update && apt-get upgrade -y

# Встановлюємо потрібні пакети
RUN apt-get install git -y && pip install pipenv

# Створюємо робочу папку
WORKDIR /lab

# Завантажуємо файли з Git
RUN git clone https://github.com/Vitalik-Khomiak/Vitalik_Khomiak_IK_31.git

# Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
WORKDIR /app
RUN cp -r /lab/Vitalik_Khomiak_IK_31/lab_3/* .

# Інсталюємо всі залежності
RUN pipenv install

# Відкриваємо порт 8000 на зовні
EXPOSE 8000

# Це команда яка виконається при створенні контейнера
ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
```

5. Створив власний репозиторій на Docker Hub. Для цього залогінився у власний аккаунт на [Docker Hub](https://hub.docker.com) після чого перейшов у вкладку Repositories і далі натиснув кнопку Create new repository. Мій репозиторій [знаходиться за адресою](https://hub.docker.com/repository/docker/artlaab/lab4).

6. Виконав білд (build) Docker імеджа та завантажив його до репозиторію. Для цього потрібно вказати правильну назву репозиторію та TAG. Оскільки мій репозиторій artlaab/lab4 то команда буде виглядати (де django - це тег): 

```python
sudo docker build -t artlaab/lab4:django
```

```python
docker images
```

```python
artlab@artlab-VirtualBox:~/PycharmProjects/Vitalik_Khomiak_IK_31/lab_4$ sudo docker images
REPOSITORY        TAG        IMAGE ID       CREATED          SIZE
artlaab/lab4      django     697b25b2c936   27 seconds ago   340MB
python            3.8-slim   214d62795dbb   2 weeks ago      122MB
docker/whalesay   latest     6b362a9f73eb   6 years ago      247MB
```

```python
docker push artlaab/lab4:django
```
Команда для завантаження на власний репозеторій docker push pavlovulchak/lab4:django.
Посилання на мій [Docker Hub](https://cloud.docker.com/repository/registry-1.docker.io/pavlovulchak/lab4) репозиторій та посилання на [імедж](https://hub.docker.com/layers/177264340/artlaab/lab4/django/images/sha256-09e787a5e91bd4267eb949a9ed0c58a42319d12d3478582332e16def0104af5b?context=repo).


7. Для запуску веб-сайту виконав команду 

```python
sudo docker run -it --name=django --rm -p 8000:8000 artlaab/lab4:django
```

Перейшов на адресу http://127.0.0.1:8000 та переконався що мій веб-сайт працює:


8. Оскільки веб-сайт готовий і працює, потрібно створит ще один контейнер із програмою моніторингу нашого веб-сайту (Моє Завдання на роботу):
    1. Створив ще один Dockerfile з назвою Dockerfile.site в якому помістив програму моніторингу.


Вміст файлу Dockerfile.site:
```python
FROM python:3.8-slim

LABEL author="Bohdan"
LABEL version=1.0

# оновлюємо систему
RUN apt-get update && apt-get upgrade -y

# Встановлюємо потрібні пакети
RUN apt-get install git -y && pip install pipenv

# Створюємо робочу папку
WORKDIR /lab

# Завантажуємо файли з Git
RUN git clone https://github.com/Vitalik-Khomiak/Vitalik_Khomiak_IK_31.git

# Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
WORKDIR /app
RUN cp -r /lab/Vitalik_Khomiak_IK_31/lab_3/* .

# Інсталюємо всі залежності
RUN pipenv install

# Відкриваємо порт 8000 на зовні
EXPOSE 8000

# Це команда яка виконається при створенні контейнера
ENTRYPOINT ["pipenv", "run", "python", "monitoring.py" , "0.0.0.0:8000"]
```

    2. Виконав білд даного імеджа та дав йому тег monitoring командами:

```python
sudo docker build -f Dockerfile.site -t artlaab/lab4:monitoring .
docker push artlaab/lab4:monitoring
```

    3.Запустив два контейнери одночасно (у різних вкладках) та переконався що програма моніторингу успішно доступається до сторінок мого веб-сайту.
Використовуючи команди:
Запуск серевера: 

```python
artlab@artlab-VirtualBox:~/PycharmProjects/Vitalik_Khomiak_IK_31/lab_4$ sudo docker run -it --name=django --rm -p 8000:8000 artlaab/lab4:django
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 14, 2021 - 16:09:50
Django version 3.2.9, using settings 'my_site.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
[14/Nov/2021 16:09:55] "GET / HTTP/1.1" 200 167
[14/Nov/2021 16:11:23] "GET /health HTTP/1.1" 301 0
[14/Nov/2021 16:11:23] "GET /health/ HTTP/1.1" 200 318
[14/Nov/2021 16:12:23] "GET /health HTTP/1.1" 301 0
[14/Nov/2021 16:12:23] "GET /health/ HTTP/1.1" 200 318

```

Запуск моніторингу:
```python

artlab@artlab-VirtualBox:~/PycharmProjects/Vitalik_Khomiak_IK_31/lab_4$ sudo docker run -it --name=monitoring --rm --net=host -v $(pwd)/server.log:/app/server.log artlaab/lab4:monitoring
[sudo] password for artlab:     
^CTraceback (most recent call last):
  File "monitoring.py", line 32, in <module>
    time.sleep(60)
KeyboardInterrupt
artlab@artlab-VirtualBox:~/PycharmProjects/Vitalik_Khomiak_IK_31/lab_4$ 

```

