FROM python:3.8.16-slim-buster

# set work directory
WORKDIR /app

#Install requirements
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./main.py /app/main.py

COPY . ./

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]