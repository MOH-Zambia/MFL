FROM python:3.7.2

LABEL Chisanga L. Siwale <Chisanga.Siwale@gmail.com>

ENV CONTAINER_PATH /var/lib/MFL

RUN mkdir /var/lib/MFL
WORKDIR $CONTAINER_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver"]