FROM python:3

ENV PYTHONIOENCODING UTF-8
ENV PYTHONUNBUFFERED 1
ENV TZ=ASIA/Bishkek

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


RUN mkdir static && mkdir media

RUN mkdir media/avatars
COPY default_avatar.jpg ./media/avatars/

COPY .. .


