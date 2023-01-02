FROM python:3

RUN apt update -y \
    && apt upgrade -y

RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . /app/

#ENV STATICFILES_HOME=/tmp/staticfiles
 
#RUN mkdir -p $STATICFILES_HOME

# WORKDIR is as `cd` + `mkdir`
#WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

#CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
