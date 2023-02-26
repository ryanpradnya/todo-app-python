FROM python:3.9-slim

WORKDIR /usr/src

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /usr/src/requirements.txt

COPY ./src /usr/src/app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
