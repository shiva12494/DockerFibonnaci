FROM python:3.7.13-slim-buster

RUN pip install "poetry" 

WORKDIR /app 

COPY . /app/  	

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi


EXPOSE 8000 

ENTRYPOINT ["python","/app/fib.py"] 