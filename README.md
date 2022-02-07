# Установка
1. Клонировать репозиторий и перейти в него в командной строке:
``
git clone 'https://github.com/Imbafar/catalog.git'
``
``
cd catalog/
``
2. Cоздать и активировать виртуальное окружение:
``
python3 -m venv venv
``
``
source venv/bin/activate
``
3. Установить зависимости из файла requirements.txt:
``
python3 -m pip install --upgrade pip
``
``
pip install -r requirements.txt
``
4. Выполнить миграции:
``
python3 manage.py makemigrations
``
``
python3 manage.py migrate
``
5. Запустить проект:
``
python3 manage.py runserver
``

# Документация

Документация для API YaMDb доступна по адресам:

``
"http://127.0.0.1:8000/swagger/"
``
``
"http://127.0.0.1:8000/redoc/"
``


# Контакты

Telegram: @AlfirFS 
