FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python","api/app.py"]

docker build -t aviation-ml-platform .
docker run -p 5000:5000 aviation-ml-platform