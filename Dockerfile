FROM python:alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8989
CMD [ "python", "run.py"]