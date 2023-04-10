FROM python:3-alpine3.16
WORKDIR /Book_keep_API
ADD . /Book_keep_API
RUN pip install -r requirements.txt
EXPOSE 5000
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz
CMD ["python","app.py"]


