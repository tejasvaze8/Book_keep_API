FROM python:3-alpine3.16
WORKDIR /usr/src/app
ADD . /Book_keep_API
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]


