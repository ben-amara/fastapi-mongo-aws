FROM python:3.8

ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

EXPOSE 80

COPY ./app /app

ENTRYPOINT ["/run_app_dev.sh"]

RUN ["chmod", "+x", "/run_app_dev.sh"]