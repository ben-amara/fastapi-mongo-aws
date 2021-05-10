FROM python:3.8

# set work directory
WORKDIR /usr/src/app

# copy project
COPY . /usr/src/app

RUN pip install -r requirements.txt --src /usr/src/app

EXPOSE 80

RUN ["python", "app/main.py"]