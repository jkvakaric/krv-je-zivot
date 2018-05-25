# Krv Je Život

2018 Combis try{code}catch hackathon task implementation by WifiCable team

- Podrebarac, David
- Močilac, Stjepan
- Kvakarić, Josip

## backend

- django-crispy-forms = "==1.7.2"
- django-enumfields = "==0.10.0"
- djangorestframework = "==3.8.2"
- boto3 = "==1.6.2"
- django-npm = "==1.0.0"
- numpy = "==1.14.3"
- aiohttp = "==3.2.1"
- sklearn = "==0.0"
- scipy = "==1.1.0"
- imblearn = "==0.0"

## frontend

- Bootstrap 3.3.7
- AdminLTE 2.4.3
- font-awesome 4.7.0
- ionicons 3.0.0
- jquery 3.3.1
- datatables.net 1.10.16
- instascan 1.0.0

## virtualenv

```
pipenv --python 3.6.x
```

## global deps

- npm
- docker
- pyenv
- pipenv
- python 3.6.x
- gulp-cli


## env

```
cp .envs/.local/.postgres.example .envs/.local/.postgres
cp .env.example .env
source .env
```

## project deps

```
npm install
pipenv update
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=<pwd> --name=postgres96 postgres:9.6
docker run -d -p 1025:1025 -p 8025:8025 --name=mailhog100 mailhog/mailhog:v1.0.0
```

## database

```
pgcli postgres://postgres:74717278@127.0.0.1:5432/
drop database krv_je_zivot
create database krv_je_zivot
```

## migrations & seeds

```
python manage.py migrate
python manage.py loaddata */fixtures/*.json
```

## runtime deps

```
docker start postgres96 mailhog100
```
alternatively
```
./MailHog
```

## start

```
gulp
```

## misc & fixes

css in - /static/sass/**/*.scss
lib/admin-lte/dist/css/img/boxed-bg.jpg - because of (https://github.com/almasaeed2010/AdminLTE/issues/1789)
