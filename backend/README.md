### API ENDPOINTS

    /api/v1/login
    /api/v1/movie/search
    /ap1/v1/authenticate

### RUN WIHOUT dockerc-compse:

    Download The project

        $ git clone https://github.com/shajalahamedcse/nc-omdb.git
        $ cd nc-omdb

    Install env ,then:

        $ python3 -m venv env
        $ source env/bin/activate
        $ cd backend
        $ pip install -r requirements.txt


    RUN postgres using docker

        $ docker run -p 5432:5432 --name postgres1 -e POSTGRES_PASSWORD=postgres  postgres


    Enter into potgres container

        $ docker exec -it {container id} /bin/sh
        $ psql -U postgres -W

    Enter Password
        $ postgres
    
    Create Database
        $ create database omdb;



### DB Migrations

        
        $ python manage.py db init
        $ python manage.py db migrate
        $ python manage.py db upgrade


### Seeder

        $ export FLASK_APP app.py
        $ flask seed run


### RUN Code

        $ python app.py

