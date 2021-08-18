# API Yatube
В приложение Yatube (социальная сеть с записями пользователей) добавлен программный интерфейс для обмена данными. Из проекта исключен frontend. 

С помощью API можно: 
- просматривать, создавать, редактировать и удалять посты, комментарии к чужим постам
- просматривать и создавать группы
- просматривать и создавать подписки на других авторов

Полная документация к API доступна по адресу: http://127.0.0.1:8000/redoc/

Следующие технологии были использованы при создании проекта:
- Python
- Django REST 
- Git

Установка:

1. Клонируем репозиторий на локальную машину: $ git clone https://github.com/Omnomus/api_final_yatube
2. Создаем виртуальное окружение: $ python -m venv venv
3. Устанавливаем зависимости: $ pip install -r requirements.txt
4. Создание и применение миграций: $ python manage.py makemigrations и $ python manage.py migrate
5. Запускаем django сервер: $ python manage.py runserver

