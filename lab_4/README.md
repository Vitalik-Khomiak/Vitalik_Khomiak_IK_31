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

