FROM python:3

WORKDIR /app

COPY ./public /app
COPY server.py /app

EXPOSE 80

CMD ["python", "server.py"]
