# Project Setup

[![Django](https://img.shields.io/pypi/l/django)](https://www.djangoproject.com/)[![MIT](https://img.shields.io/pypi/l/mit)](https://opensource.org/license/mit)[![Docker](https://img.shields.io/pypi/l/docker)](https://www.docker.com/)[![Repo](https://img.shields.io/github/commit-activity/w/rzmobiledev/anbk/main)](https://github.com/rzmobiledev/anbk)

## Run Locally

Clone the project

```bash
  git clone https://github.com/rzmobiledev/anbk.git
```

Go to the project directory

```bash
  cd anbk
```

I would recommend to use python version 3.10.5 as all dependencies within this project based on that version.

```bash
python -V
Python 3.10.5
```

Create and activate python environment for Linux/Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

Create and activate python environment for Windows

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### Install dependencies.

```bash
  pip install -r requirements_new.txt
```

Create `.env` file

```bash
cp env.dev .env
```

Run Unit test

```bash
pytest
```

Make migration (Optional)

```bash
python ./manage.py makemigrations
python ./manage.py migrate
```

Start the server

```bash
python manage.py runserver 3001
```

# Run With Docker

Make sure you already install docker desktop before running execution.

Go to the project directory

```bash
cd anbk
```

Create `.env` file

```bash
rm .env
cp env.prod .env
```

Run Docker

```bash
docker compose up -d
```

## Django Admin Login

If you run docker, your django admin credentials is:

```bash
username : admin
password: admin123
```

if you run local, you can stop running server and create a superuser access.

```bash
python manage.py createsuperuser
```

## Swagger Endpoint

Swagger API is available at `http://127.0.0.1:3001/api/swagger/`

![image](https://i.imghippo.com/files/igeX5263bY.png)

## Demo

To demonstrate Front End, kindly access to `http://127.0.0.1:3001`.

![image](https://i.imghippo.com/files/Yytb2336.png)

![image](https://i.imghippo.com/files/dV7173vMc.png)

![image](https://i.imghippo.com/files/QZnK8693vs.png)

![image](https://i.imghippo.com/files/Kcg2387cw.png)

![image](https://i.imghippo.com/files/MYXO8469pIQ.png)

## Report

In case you find error, kindly email me ASAP rzmobiledev@gmail.com

Thank you

### Safrizal
