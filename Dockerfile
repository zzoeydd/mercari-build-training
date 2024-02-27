FROM python:3.12.2

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV NAME World

CMD ["python", "app.py"]
