FROM python:3-alpine3.16
WORKDIR /Book_keep_API
ADD . /Book_keep_API
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["python","app.py"]


