FROM python:3.8-slim

WORKDIR /app
ADD . /app
COPY . .

EXPOSE 5000
ENV UWSGI_CHEAPER 0
ENV UWSGI_PROCESSES 1
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=0
RUN pip install -r requirements.txt

CMD ["python","app.py"]