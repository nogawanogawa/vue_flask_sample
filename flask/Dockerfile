FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip3 install mysql-connector-python
RUN pip3 install flask_cors

ADD . /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV MYSQL_DATABASE=sample_db
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

ENV FLASK_APP app.py
CMD [ "flask", "run", "--host=0.0.0.0", "--port=80"]

