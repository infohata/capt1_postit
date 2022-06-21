# syntax=docker/dockerfile:1

FROM python:slim-buster
WORKDIR /app
COPY ./requirements.txt .
COPY ./drf_api_project .
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
