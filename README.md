# Проект REST API для Yatube
## Описание проекта:
**Yatube** - Платформа для публикации постов, комментариев, подписок и работы с сообществами.
**API** позволяет пользователям создавать и просматривать посты, комментировать их, подписываться на других пользователей, а также получать JWT-токены для авторизации.
## Стек:
- Python 3.9
- Django 3.2
- Django REST Framework 3.12
- Djoser (аутентификация)
- Simple JWT (токены)
## Возможности:
- JWT-авторизация и аутентификация пользователей
- Публикации: создание, получение, редактирование, удаление
- Комментарии: добавление, редактирование, удаление
- Подписки между пользователями
- Работа с группами (сообществами)
- Пагинация: поддержка limit и offset
## Установка и запуск:
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
## Примеры запросов к API:
### Создание пользователя:
```POST /auth/users/```
Тело запроса:
```
{
    "username": "string"
    "password": "string"
}
```
### Получение токена:
```POST /api/v1/jwt/create/```
Тело запроса:
```
{
    "username": "string"
    "password": "string"
}
```
### Создание публикации:
```POST /api/v1/posts/```
Тело запроса:
```
{
    "text": "Текст",
    "image": null,
    "group": 1
}
```
### Получение всех публикаций:
```GET /api/v1/posts/```
### Редактирование публикации:
```PUT /api/v1/posts/{id}/```
```
{
    "text": "Новый текст",
    "image": null,
    "group": 1
}
```
### Удаление публикации:
```DELETE /api/v1/posts/{id}/```
### Получение комментариев:
```GET /api/v1/posts/{id}/comments/```
### Добавление комментария:
```POST /api/v1/posts/{id}/comments/```
Тело запроса:
```
{
    "text": "Комментарий"
}
```
### Подписание на пользователя:
```POST /api/v1/follow/```
Тело запроса:
```
{
    "following": "username"
}
```
## Документация:
Полная документация доступна по адресу:
http://127.0.0.1:8000/redoc/
## Автор:
### Игорь Журавлев
Ссылка на GitHub:
https://github.com/sijey06