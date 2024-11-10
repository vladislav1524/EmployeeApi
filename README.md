# EmplyeeApi
## Описание проекта 📄:
В рамках тестового задания разработана REST API для управления данными с использованием Python, Django и Django REST Framework (DRF). Проект включает модели данных для сотрудников и департаментов. API позволяет получать списки сотрудников и департаментов, фильтровать сотрудников по фамилии и ID департамента, добавлять и удалять сотрудников, а также предоставляет пагинацию для списка сотрудников. Доступ к списку сотрудников ограничен авторизованными пользователями, департаменты могут просматривать все. Реализована админ-панель для управления данными и Swagger-документация для API методов.

## Используемые технологии 🧑‍💻:
- Python
- Django
- Django REST Framework (DRF)
- Swagger (для документации API)

## Как запустить проект 🛠️:
1. Создадите файл .env на уровне с manage.py
пример .env:
```
DEBUG=True
SECRET_KEY=ваш_секретный_ключ
```
2. После активации виртуального окружение установите зависимости:
```bash
pip install -r requirements.txt
```
3. Создание суперпользователя:
```bash
python manage.py createsuperuser
```
4. Запуск проекта:
```bash
python manage.py runserver
```

## Задание:

![Тз](https://ltdfoto.ru/images/2024/11/10/SNIMOK-EKRANA-2024-11-10-092658.png)

Задание взято с https://gitlab.com/Illuzzion/employee_department/-/blob/ba405f3b8ea3ba496939f9ab65ca9856fd9e7d3e/Тестовое%20задание%20для%20Python_Django_DRF%20разработчика.pdf
