FROM python:3.5-alpine
MAINTAINER Vitalii Vokhmin <vitaliy.vokhmin@gmail.com>

RUN mkdir -p /usr/src
WORKDIR /usr/src

COPY requirements.txt /usr/src/
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src /usr/src

ENV TG_BOT_TOKEN ''
ENV TG_BOT_NAME 'HelloEP17Bot'

CMD [ "python", "app.py" ]
