FROM docker.io/library/python:3.7-alpine
WORKDIR /app
EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . .
CMD ["flask", "run"]