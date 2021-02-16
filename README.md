# Foodgram


![foodgram-project](https://github.com/tuda-suda/foodgram-project/workflows/Foodgram/badge.svg)


### Description
Foodgram is a site that lets you create your own recipes and share them with other people. You can also subscribe to recipe authors and add recipes to your shop-list - 
and download the list with all ingredients you need.

The site is available on http://84.201.159.80


## Tech stack
- Python 3.8
- Django and Django Rest Framework
- PostgreSQL
- Gunicorn + Nginx
- CI/CD: Docker, docker-compose, GitHub Actions
- Yandex.Cloud

## Setup
- Clone the github repository
    ```
    git clone https://github.com/tuda-suda/foodgram-project.git
    ```
- Enter the project directory
    ```
    cd foodgram-project/
    ```
- Start docker-compose
    ```
    docker-compose -f docker-compose.yaml up -d
    ```
- Create superuser
    ```
    docker-compose -f docker-compose.yaml run --rm web python manage.py createsuperuser
    ```
### Optional
- Load test data
    ```
    docker-compose -f docker-compose.yaml run --rm web python manage.py loaddata fixtures.json
    ```
