FROM python:3.8.16-slim-buster

# set work directory
WORKDIR /app

#Install requirements
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./app.py /app/app.py

COPY . ./

CMD ["python", "app.py"]

