FROM python:3.10.12

WORKDIR /app

COPY ./requirements/dev.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r dev.txt

COPY ./src .
COPY ./.env .

CMD [ "python", "src/main.py" ]

EXPOSE 8080