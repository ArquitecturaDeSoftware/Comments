FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD ./requirements.txt /code/requirements.txt
 RUN pip3 install -r requirements.txt
 ADD . /code/
 EXPOSE 8000
 COPY entrypoint.sh /entrypoint.sh
 RUN chmod +x /entrypoint.sh
