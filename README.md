# Blogicum

## Описание
Социальная сеть для публикации коротких записей.

## Функционал сайта
Пользователь может зарегистрироваться и создавать посты (записи).
Для каждого можно выбрать категорию и указать локацию.


## Установка и запуск проекта

Клонировать репозиторий:
```
git clone <https or SSH URL>
```

Перейти в папку проекта:
```
cd django_sprint3
```

***
### 1. Автоматическая установка
Запустить скрипт и следовать инструкциям:
```
bash install.sh
```

***
### 2. Мануальная установка
Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/bin/activate
```

Обновить pip:
```
python -m pip install --upgrade pip
```

Установить библиотеки:
```
pip install -r requirements.txt
```

Выполнить миграции:
```
python blogicum/manage.py migrate
```

Загрузить фикстуры DB:
```
python blogicum/manage.py loaddata db.json
```

Создать суперпользователя:
```
python blogicum/manage.py createsuperuser
```

Запустить сервер django:
```
python blogicum/manage.py runserver
```
