FROM python:3.6

ENV USR nonroot
ENV HOME /home/$USR
ENV PROJECT_DIR $HOME/code
ENV PYTHONUNBUFFERED 1

EXPOSE 5000

RUN groupadd -g 1000 -r $USR && \
  useradd -u 1000 -d $HOME -m -r -g $USR $USR

RUN pip install --no-cache-dir \
  empty==0.4.3\
  eventlet==0.21.0\
  flask-jsglue==0.3.1\
  flask-marshmallow==0.8.0\
  flask-migrate==2.0.4\
  flask-restful==0.3.6\
  flask-security==3.0.0\
  flask-socketio==2.8.6\
  flask-sqlalchemy==2.2\
  flask-rq2\
  marshmallow-sqlalchemy==0.13.1\
  psycopg2==2.7.1\
  redis==2.10.5

RUN mkdir $PROJECT_DIR
WORKDIR $PROJECT_DIR
COPY --chown=1000:1000 . .

USER $USR
CMD ["flask", "run", "-h", "0.0.0.0"]