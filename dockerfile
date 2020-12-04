FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip3 install -r /app/requirements.txt
EXPOSE 8080
CMD [ "python3" , "api.py" ]