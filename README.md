# Bookstore

Bookstore APP from Backend Python course from EBAC

## Prerequisites

```
Python 3.5>
Poetry
Docker && docker-compose

```

## Quickstart

1. Clone this project

   ```shell
   git clone git@github.com:drsantos20/bookstore.git
   ```

2. Install dependencies:

   ```shell
   cd bookstore
   poetry install
   ```

3. Run local dev server:

   ```shell
   poetry run manage.py migrate
   poetry run python manage.py runserver
   ```
   
4. Run docker dev server environment:

   ```shell
   docker-compose up -d --build 
   docker-compose exec web python manage.py migrate
   ```

5. Run tests inside of docker:

   ```shell
   docker-compose exec web python manage.py test
   ```