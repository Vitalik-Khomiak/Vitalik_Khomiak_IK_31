# **Лабораторна робота №5**
---
	Послідовність виконання лабораторної роботи:
1. Для ознайомляння з `docker-compose` звернувся до документації.
Щоб встановити `docker-compose` використав команди:
```text
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
2. Ознайомився з бібліотекою `Flask`, яку найчастіше використовують для створення простих веб-сайтів на Python.
3. Моє завдання: за допомогою Docker автоматизувати розгортання веб сайту з усіма супутніми процесами. Зроблю я це двома методами: 
* за допомогою `Makefile`;
* за допомогою `docker-compose.yaml`.

4. Першим розгляну метод з `Makefile`, але спочатку створю робочий проект.
5. Створив папку `my_app` в якій буде знаходитись мій проект. Створив папку `tests` де будуть тести на перевірку працездатності мого проекту. Скопіював файли `my_app/templates/index.html`, `my_app/app.py `, `my_app/requirements.txt`, `tests/conftest.py`, `tests/requirements.txt`, `tests/test_app.py` з репозиторію викладача у відповідні папки мого репозеторію. Ознайомився із вмістом кожного з файлів. Звернув увагу на файл requirements.txt у папці проекту та тестах. Даний файл буде мітити залежності для мого проекту він містить назви бібліотек які імпортуються.







6. Я спробував чи проект є працездатним перейшовши у папку `my_app` та після ініціалізації середовища виконав команди записані нижче:
```text
sudo pipenv --python 3.8
sudo pipenv install -r requirements.txt
sudo pipenv run python app.py
```

1. Так само я ініціалузував середовище для тестів у іншій вкладці шелу та запустив їх командою `sudo pipenv run pytest test_app.py --url http://localhost:5000` але спочатку треба перейти в папку `tests`:
    ```text
    ik31@ik31-VirtualBox:~/Desktop/Vitalik_Khomiak_IK_31/lab_5/tests$ sudo pipenv run pytest test_app.py --url http://localhost:5000
============================================= test session starts ==============================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/ik31/Desktop/Vitalik_Khomiak_IK_31/lab_5/tests
collected 4 items                                                                                              

test_app.py ..FF                                                                                         [100%]

=================================================== FAILURES ===================================================
__________________________________________________ test_logs ___________________________________________________

url = 'http://localhost:5000'

    def test_logs(url):
        response = requests.get(url + '/logs')
>       assert 'My Hostname is:' in response.text, 'Logs do not have Hostname'
E       AssertionError: Logs do not have Hostname
E       assert 'My Hostname is:' in '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n  "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n  ...en(\'logs/app.log\', \'r\') as log:\nFileNotFoundError: [Errno 2] No such file or directory: \'logs/app.log\'\n\n-->\n'
E        +  where '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n  "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n  ...en(\'logs/app.log\', \'r\') as log:\nFileNotFoundError: [Errno 2] No such file or directory: \'logs/app.log\'\n\n-->\n' = <Response [500]>.text

test_app.py:27: AssertionError
________________________________________________ test_main_page ________________________________________________

url = 'http://localhost:5000'

    def test_main_page(url):
        response = requests.get(url)
>       assert 'You are at main page.' in response.text, 'Main page without text'
E       AssertionError: Main page without text
E       assert 'You are at main page.' in '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n  "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n  ...)\nredis.exceptions.ConnectionError: Error -3 connecting to redis:6379. Temporary failure in name resolution.\n\n-->\n'
E        +  where '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n  "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n  ...)\nredis.exceptions.ConnectionError: Error -3 connecting to redis:6379. Temporary failure in name resolution.\n\n-->\n' = <Response [500]>.text

test_app.py:32: AssertionError
=========================================== short test summary info ============================================
FAILED test_app.py::test_logs - AssertionError: Logs do not have Hostname
FAILED test_app.py::test_main_page - AssertionError: Main page without text
========================================= 2 failed, 2 passed in 0.12s ==========================================

    ```
2. Звернув увагу, що в мене автоматично створюються файли `Pipfile` та `Pipfile.lock`, а також на хост машині буде створена папка `.venv`. Після зупинки проекту видалив їх.
3. Перевірив роботу сайту перейшовши головну сторінку. Сайт не працює бо на відсутній `redis`.











7. Видалив файли які постворювались після тестового запуску. Щоб моє середовище було чистим, все буде створюватись і виконуватись всередині Docker. Створив два файла `Dockerfile.app`, `Dockerfile.tests` та `Makefile` який допоможе автоматизувати процес розгортання.
8. Скопіював вміст файлів `Dockerfile.app`, `Dockerfile.tests` та `Makefile` з репозиторію викладача та ознайомився із вмістом `Dockerfile` та `Makefile` та його директивами. 
Вміст файла `Dockerfile.app`:
```text
FROM python:3.8-slim
LABEL author="ArtLab"

# оновлюємо систему та встановлюємо потрібні пакети
RUN apk update \
    && apk upgrade \
    && apk add git \
    && pip install pipenv

WORKDIR /app

# Копіюємо файл із списком пакетів які нам потрібно інсталювати
COPY my_app/requirements.txt ./
RUN pipenv install -r requirements.txt

# Копіюємо наш додаток
COPY my_app/ ./

# Створюємо папку для логів
RUN mkdir logs

EXPOSE 5000

ENTRYPOINT pipenv run python app.py
```
Вміст файла `Dockerfile.tests`:
```text
FROM python:3.8-slim
LABEL author="ArtLab"

# оновлюємо систему та встановлюємо потрібні пакети
RUN apk update \
    && apk upgrade \
    && apk add git \
    && pip install pipenv

WORKDIR /tests

# Копіюємо файл із списком пакетів які нам потрібно інсталювати
COPY tests/requirements.txt ./
RUN pipenv install -r requirements.txt

# Копіюємо нашого проекту
COPY tests/ ./

ENTRYPOINT pipenv run pytest test_app.py --url http://app:5000
```
Вміст файла `Makefile`:
```text
STATES := app tests
REPO := pavlovulchak/lab4

.PHONY: $(STATES)

$(STATES):
	@docker build -f Dockerfile.$(@) -t $(REPO):$(@) .

run:
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm --name app --net=appnet -p 5000:5000 -d $(REPO):app

test-app:
	@docker run --rm -it --name test --net=appnet $(REPO):tests
	
docker-prune:
	@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force
```
Дерективи `app` та `tests`:
Створення імеджів для сайту та тесту відповідно.
Деректива `run`:
Запускає сторінку сайту.
Деректива `test-app`:
Запуск тесту сторінки.
Деректива `docker-prune`:
Очищення іміджів, контейнера і інших файлів без тегів.
9. Для початку, використовуючи команду `sudo make app` створіть Docker імеджі для додатку та для тестів `sudo make tests`. Теги для цих імеджів є з моїм Docker Hub репозиторієм. Запустив додаток командою `sudo make run` та перейшовши в іншу вкладку шелу запустіть тести командою `sudo make test-app`.
Запуск сайту
```text
ik31@ik31-VirtualBox:~/Desktop/Vitalik_Khomiak_IK_31/lab_5$ sudo make run
81cc0586523385fc7150c02a4b7dc0f59dff77b873e3c2fb9fafa8f7270cfc53
Unable to find image 'redis:latest' locally
latest: Pulling from library/redis
eff15d958d66: Already exists 
1aca8391092b: Pull complete 
06e460b3ba1b: Pull complete 
def49df025c0: Pull complete 
646c72a19e83: Pull complete 
db2c789841df: Pull complete 
Digest: sha256:619af14d3a95c30759a1978da1b2ce375504f1af70ff9eea2a8e35febc45d747
Status: Downloaded newer image for redis:latest
32096d57a6cb29fb198f5789d3c0c0ceb9d2aab2d6ef70ea174caeee420e6cde
b77c20374b2b4160f3c96995152f07ff405963e9529267b7624913b37b3943ed

```
Проходження тесту:
```text
ik31@ik31-VirtualBox:~/Desktop/Vitalik_Khomiak_IK_31/lab_5$ sudo make test-app
============================= test session starts ==============================
platform linux -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /tests
collected 4 items                                                              

test_app.py ....                                                         [100%]

============================== 4 passed in 0.11s ===============================

```


10. Зупинив проект натиснувши Ctrl+C та почистив всі ресурси `Docker` за допомогою `make`.
```text
ik31@ik31-VirtualBox:~/Desktop/Vitalik_Khomiak_IK_31/lab_5$ sudo make docker-prune
b77c20374b2b
32096d57a6cb
Total reclaimed space: 0B
Deleted Volumes:
2a0121691ec7214be640a83695be8fee3ad212f785515bf7d62fa7456eaba3d9
3de94b25fc6f5a41f555c40868041e27899c3312a415d320f0646a2c47a19ed9
78ed162f58deef287084dec06b63bdb2f58c87f8f50b266036a0975ab070d96f

Total reclaimed space: 0B
Deleted Networks:
appnet

Total reclaimed space: 0B

```

11. Створив директиву `docker-push` в Makefile для завантаження створених імеджів у мій Docker Hub репозиторій.
Деректива `docker-push`:
```text
docker-push:
	@docker login \
	&& docker push $(REPO):app \
	&& docker push $(REPO):tests
```

12. Видалив створені та закачані імеджі. Команда `docker images` виводить пусті рядки. Створив директиву в Makefile яка автоматизує процес видалення моїх імеджів.
Деректива `images-delete`:
```text
images-delete:
	@docker rmi $$(docker images -q)
```
Запуск:
```text
ik31@ik31-VirtualBox:~/Desktop/Vitalik_Khomiak_IK_31/lab_5$ sudo docker images
REPOSITORY     TAG        IMAGE ID       CREATED         SIZE
artlaab/lab4   tests      3d7d3d0d6424   6 minutes ago   301MB
artlaab/lab4   app        469515e81511   6 minutes ago   300MB
redis          latest     40c68ed3a4d2   9 days ago      113MB
python         3.8-slim   64458f531a7e   10 days ago     122MB
ik31@ik31-VirtualBox:~/Desktop/Vitalik_Khomiak_IK_31/lab_5$ sudo make images-delete
Untagged: artlaab/lab4:tests
Deleted: sha256:3d7d3d0d64243d2faf7a34050cc496aae96488fa8195f06229f87d8fcd883cb1
Deleted: sha256:e79df5438ef44f545fb81211f09f11a1160ed8d791e7128980148e99e5276d34
Deleted: sha256:fd82284be3e81b22d9a1caaccd57507d2a119137682c2afc55719a0471d4907a
Deleted: sha256:8151efbf1be7cb217686086175dae75658ec68f6e6d519b4aa5cec2b4c9afb00
Deleted: sha256:2bdeade5d8f5ab81a60c930e1fd1e173ce1334aca4f6f5640ede79fa35e50a6c
Deleted: sha256:e5bc66cb506492ed916bb46c6e387846fd02983aacc172ac38313f6326b115c3
Deleted: sha256:ea0e0b77b9284efa86cfe3540a8648bcd8a052af2fec6eb8c35ac916ae90ed79
Deleted: sha256:54838906711e1143f981f0065dacabf69cf97803fc1534132c064ac76a39c1e6
Deleted: sha256:4a637c20b5d046d24213ec355770b2ec5af5226c909f2bd9a59b008ce4b7faf9
Untagged: artlaab/lab4:app
Deleted: sha256:469515e81511738bf6a4daf8e5f854bf200bf650c3b14363b3500df029f08d96
Deleted: sha256:e9c130cfefb2a5a1aa210efe2837abedebcbe73ea9caf8f303257faaffcee078
Deleted: sha256:083de42859aabec013bcd6a161dd6757201001f377686a25776bb3d5fabeb0dc
Deleted: sha256:61ab3ef59ff031a19e8136f6a96df9c062a3b60b08457258455e94a65cce803c
Deleted: sha256:1b6830efb62e734b594926889bcbf6a786497c23c5d3e46a5415e0b43e49303c
Deleted: sha256:7ed5d3189a9536f6bfc5633c768af5f9ae742d4394b96b7358742f73d412a124
Deleted: sha256:c429e5363e1b0482a68ded041993fa40dc2765767f78b6fa723909c78a0ea367
Deleted: sha256:caf1052d768d10eca4688b3c6688023b0f78c9e77e3a00b3f4d5ced2e947c655
Deleted: sha256:5f38706a4f4677f32ca17479bb6220d734db58e5ce1f9e846599156734956657
Deleted: sha256:6383be637a62fec1c91a353c81df0aa2506f7edb89efbac2583c70231f391589
Deleted: sha256:5150833108b86a2c11593387c1b559f9c8cd754e6d3f27fa4424695daf680cc8
Deleted: sha256:7f674cec5f523f9934f7601a92c62dd356830258655a5badcb1c7e1e34a7fb96
Deleted: sha256:8ebb223dec1b51c527d4bc67874793b7252b89963911c31cb429b4102c95208f
Deleted: sha256:b46d088b47d2495deaf5ad958ab16e14dce6e5121fd1ea6e7e31fce75f7a5359
Deleted: sha256:5181ef43af81b421d17d74bfca3359e2c3da4e327ba845cbd0e37f9fb634f28f
Untagged: redis:latest
Untagged: redis@sha256:619af14d3a95c30759a1978da1b2ce375504f1af70ff9eea2a8e35febc45d747
Deleted: sha256:40c68ed3a4d246b2dd6e59d1b05513accbd2070efb746ec16848adc1b8e07fd4
Deleted: sha256:bec90bc59829e7adb36eec2a2341c7d39454152b8264e5f74988e6c165a2f6a2
Deleted: sha256:c881a068a82210f7964146ebc83e88889224831178f4b8a89ddb0fba91fe96cd
Deleted: sha256:8e9a414cbe1dc316cfa02c0ee912b9c0af0e086accda4e2f340a10c4870a5b35
Deleted: sha256:37d8a78bebeb894e21a8c3bd9041bd4fb600e77154fbb58491d57ef6e70584d5
Deleted: sha256:e8755b67e77af585d946a6078463f45313ec0f385bebdb5bbebadaafbe3b4a2c
Untagged: python:3.8-slim
Untagged: python@sha256:87cdfdbf66e79dfb1d33aca671f9bee623e3710b1f6e0b8476c98c669d69deec
Deleted: sha256:64458f531a7ebebc96b2ee5d0336b71437d8addc06b6e8b463c59af2048fa5ba
Deleted: sha256:f9f986658f04ce35ae016a13d6d9392acb4d62d294c9cb529b244092d418c077
Deleted: sha256:ac8bcc28c85def48851983a79715f36655f0b5bce310750bfff4d5f097a22beb
Deleted: sha256:9b1e7d4635b373da10d62e1bcc167080c654945f29bd1162fc8c4d04382c92ae
Deleted: sha256:ba89ed484769dc64767ad3d260de7b9a0554177d72e258985b2e8cdee2f083d9
Deleted: sha256:e1bbcf243d0e7387fbfe5116a485426f90d3ddeb0b1738dca4e3502b6743b325
ik31@ik31-VirtualBox:~/Desktop/Vitalik_Khomiak_IK_31/lab_5$ 

```

13. Перейшов до іншого варіанту з використанням `docker-compose.yaml`. Для цього створив даний файл у кореновій папці проекту та заповнив вмістом з прикладу. Проект який я буду розгортити за цим варіантом трохи відрізняється від першого тим що у нього зявляється дві мережі: приватна і публічна.
Файл `docker-compose.yaml`:
```text
version: '3.8'
services:
  hits:
    build:
      context: .
      dockerfile: Dockerfile.app
    image: artlaab/lab4:compose-app
    container_name: app
    depends_on:
      - redis
    networks:
      - public
      - secret
    ports:
      - 80:5000
    volumes:
      - hits-logs:/hits/logs
  tests:
    build:
      context: .
      dockerfile: Dockerfile.tests
    image: pavlovulchak/lab4:compose-tests
    container_name: tests
    depends_on:
      - hits
    networks:
      - public
  redis:
    image: redis:alpine
    container_name: redis
    volumes:
      - redis-data:/data
    networks:
      - secret
volumes:
  redis-data:
    driver: local
  hits-logs:
    driver: local

networks:
  secret:
    driver: bridge
  public:
    driver: bridge
```

14. Перевірив чи `Docker-compose` встановлений та працює у моїй системі, а далі просто запускаю `docker-compose`:
```text
docker-compose --version
sudo docker-compose -p lab5 up
```
```text
09:25:32 pavlovulchak ~/TPIS/Pavlo_Vulchsak_IK_31/Lab5 (master) $ docker-compose --version
docker-compose version 1.29.2, build 5becea4c
09:33:50 pavlovulchak ~/TPIS/Pavlo_Vulchak_IK_31/Lab5 (master) $
```

15. Перевірив чи працює веб-сайт. Дана сторінка відображається за адресою `http://172.20.0.2:5000/`

16. Перевірив чи компоуз створив докер імеджі. Всі теги коректні і назва репозиторія вказана коректно:
```text
ik31@ik31-VirtualBox:~/Desktop/Vitalik_Khomiak_IK_31/lab_5$ sudo docker images
[sudo] password for ik31: 
REPOSITORY              TAG             IMAGE ID       CREATED         SIZE
artlaab/lab4            compose-tests   0938f2c19d0b   3 minutes ago   301MB
artlaab/lab4            compose-app     498a00869786   3 minutes ago   299MB
python                  3.8-slim        64458f531a7e   10 days ago     122MB
redis                   alpine          5c08f13a2b92   2 weeks ago     32.4MB

```

17. Зупинив проект натиснувши `Ctrl+C` і почистітив ресурси створені компоуз командою `docker-compose down`.

18. Завантажив створені імеджі до Docker Hub репозиторію за допомого команди `sudo docker-compose push`.

19. Що на Вашу думку краще використовувати `Makefile` чи `docker-compose.yaml`? - На мою думку `Makefile` при використанні більш інтуїтивно зрозумілий, адже можна в ньому побачити які команди запускаються, але і в одночас треба знати які команди використовувати. На рахунок `docker-compose.yaml` він менш зрозуміліший і там не показано команди які потрібно запустити а лише вказано що потрібно запусти, підклучити чи збілдити і користувача не хвилює як воно це робить. Як для мене мені обидва методи добрі.

20. (Завдання) Оскільки Ви навчились створювати docker-compose.yaml у цій лабораторній то потрібно:
- Cтворив `docker-compose.yaml` для лабораторної №4. Компоуз повинен створити два імеджі для `Django` сайту та моніторингу, а також їх успішно запустити.
Файлик `docker-compose.yaml`:
```text
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    image: artlaab/lab4:compose-jango
    container_name: django
    networks:
      - public
    ports:
      - 8000:8000
  monitoring:
    build:
      context: .
      dockerfile: Dockerfile.site
    image: artlaab/lab4:compose-monitoring
    container_name: monitoring
    network_mode: host

networks:
  public:
    driver: bridge
```
21. Після успішного виконання роботи я відредагував свій `README.md` у цьому репозиторію та створив pull request.
