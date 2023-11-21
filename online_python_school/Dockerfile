FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

WORKDIR /online_python_school

COPY . .

RUN apk update \
	&& apk add bash \
	&& apk add postgresql-client

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["/online_python_school/run_webapp.sh"]

