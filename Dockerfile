FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY /. .

RUN apt update && apt install wkhtmltopdf -y
RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT [ "/app/entrypoint.sh" ]