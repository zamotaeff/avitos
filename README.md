# Тестовый проект на Django

### Запуск

- Находимся в папке проекта
- poetry shell
- poetry install
- cd postgres
- docker-compose up -d
- cd ..
- cd project
- python3 manage.py migrate
- python3 manage.py csv_to_json
- python3 manage.py add_new_locations
- python3 manage.py add_new_users
- python3 manage.py add_new_categories
- python3 manage.py add_new_ads
- python3 manage.py createsuperuser
- python3 manage.py runserver
