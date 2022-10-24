# Django Test Project (D'avito)

## Start project

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

## Tests

- cd project
- python3 manage.py test ads
- python3 manage.py test users

## Routes

### Ad

- ad/ - shows a list of ads (?page param of request for pagination)
- ad/create/ - post request for create new ad
- ad/id/ - shows details of ad by id
- ad/id/delete/ - delete ad by id
- ad/id/update/ - update ad by id
- ad/id/upload_image/ - upload image for ad

### Category

- cat/ - shows a list of categories
- cat/create/ - post request for create new category
- cat/id/ - shows details of category by id
- cat/id/delete/ - delete category by id
- cat/id/update/ - update category by id

### User
- user/ - shows a list of users (?page param of request for pagination)
- user/create/ - post request for create new user
- user/id/ - shows details of user by id
- user/id/delete/ - delete user by id
- user/id/update/ - update user by id
