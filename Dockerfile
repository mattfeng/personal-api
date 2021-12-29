FROM python:3.8.12-buster

WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./main.py /app
ENTRYPOINT ["gunicorn"]
CMD ["--bind", "0.0.0.0:4000", "main:create_app()"]