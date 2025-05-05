# Проект REST API для Yatube
---
## Описание проекта:
---
**Yatube** - Платформа для публикации постов, комментариев, подписок и работы с сообществами.
**API** позволяет пользователям создавать и просматривать посты, комментировать их, подписываться на других пользователей, а также получать JWT-токены для авторизации.
## Стек:
---
- Python 3.9
- Django 3.2
- Django REST Framework 3.12
- Djoser (аутентификация)
- Simple JWT (токены)
## Установка и запуск:
---
1. Клонировать репозиторий и перейти в него:
```
git clone https://github.com/sijey06/api_final_yatube.git
```
```
cd api_final_yatube
```
2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
```
python -m pip install --upgrade pip
```
3. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
4. Создать и применить миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
5. Запустить проект:
```
python manage.py runserver
```