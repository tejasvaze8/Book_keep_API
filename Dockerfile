FROM python:3-alpine3.16
WORKDIR /API
ADD . /API
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]


