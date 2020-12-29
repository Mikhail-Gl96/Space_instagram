# Космический Инстаграм

Задача проекта - автоматизировать выгрузку изображений с сайта SpaceX и Hubble с их последующей автоматической загрузкой в аккаунт инстаграмма 

#### Бот работает с версиями Python 3.6+ <br>С версиями ниже бот не работает!!!

## Настройка для использования на личном ПК
1. Скачайте проект с гитхаба
2. Перейдите в папку с ботом с помощью консоли и команды `cd <путь до проекта>`<br>
3. Установить зависимости из файла `requirements.txt`<br>
   Библиотеки к установке: `requests`, `instabot`, `python-dotenv`, `pillow`.<br>
   
   Возможные команды для установки:<br>
   `pip3 install -r requirements.txt`<br>
   `python -m pip install -r requirements.txt`<br>
   `python3.6 -m pip install -r requirements.txt`
4. Создайте файл .env
5. Запишите в файл .env переменные:
    `LOGIN_INSTAGRAM=ваш_логин_от_инстаграмм_аккаунта`<br>
    `PASSWORD_INSTAGRAM=ваш_пароль_от_инстаграмм_аккаунта`<br>
6. Запустите бота<br>
   Возможные команды для запуска(из консоли, из папки с ботом):<br>
   `python3 main.py`<br>
   `python main.py`<br>
   `python3.6 main.py`<br>
 
Instagram: https://www.instagram.com/deep_spacebot/

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).