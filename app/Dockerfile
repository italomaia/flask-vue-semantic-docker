FROM python:3.6

ENV USR nonroot
ENV HOME /home/$USR
ENV FLASK_PORT 5000

EXPOSE $FLASK_PORT

RUN groupadd -g 1000 -r $USR && \
  useradd -u 1000 -d $HOME -m -r -g $USR $USR

WORKDIR $HOME

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chown -R 1000:1000 .

USER $USR
CMD ["flask", "run", "-h", "0.0.0.0"]