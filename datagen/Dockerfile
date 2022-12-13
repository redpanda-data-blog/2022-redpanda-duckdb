FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ADD user_payments_generator.py .

ENV RUNTIME_ENVIRONMENT="DOCKER"

CMD ["python", "/app/user_payments_generator.py"]