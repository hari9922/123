FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8089

ENTRYPOINT ["python3"]

CMD ["/app/apppy.py"]
