# krv-je-zivot

krv-je-zivot

## na backend-u koristimo

- django-crispy-forms = "==1.7.2"
- django-enumfields = "==0.10.0"
- celery = "==3.1.26.post2"
- djangorestframework = "==3.8.2"
- boto3 = "==1.6.2"

## na frontend-u koristimo

- Bootstrap 3.3.7
- AdminLTE 2.4.3
- font-awesome 4.7.0
- ionicons 3.0.0
- jquery 3.3.1

## virtualenv

```
pipenv --python 3.6.5
```

## global deps

node npm mailhog docker pyenv pipenv python3.6.5 gulp-cli

```
node -v ( v8.x.x )
python -V ( Python 3.6.5 )
```

```
npm install -g gulp-cli
```

## env i virtualenv

virtualenv path treba promjeniti u .env file-u
u .postgres postaviti sifru i usera

```
cp .envs/.local/.postgres.example .envs/.local/.postgres
cp .env.example .env
source .env
```

## project deps

```
npm install
pipenv update  # kod pokretanja se mora biti u folderu projekta
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=<pwd> --name=postgres96 postgres:9.6
docker run -d -p 1025:1025 -p 8025:8025 --name=mailhog100 mailhog/mailhog:v1.0.0
```
u docker naredbi napisati sifru za default usera (postgres)

## recreate db

```
drop database krv_je_zivot
create database krv_je_zivot
```

## nakon update-a modela (db sloj)

```
python manage.py migrate  # ubacivanje promjena tablica u bazu
python manage.py loaddata */fixtures/*.json  # ubacivanje inicijalnih podataka u bazu
```

## runtime

```
docker start postgres96 mailhog100
```
ili
```
./MailHog  # ako je MailHog instaliran kao binary
```

## start

```
gulp  # pokrece se uvijek iz root-a projekta i iz terminala gdje je aktiviran virtualenv
```

## misc

css ide u - /static/sass/*.scss
lib/admin-lte/dist/css/img/boxed-bg.jpg - ova slika je tu zbog (https://github.com/almasaeed2010/AdminLTE/issues/1789)
