
FROM python:3.7

RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app


# ENV FLASK_APP app.py

EXPOSE 5000

CMD ["python3", "app.py"]