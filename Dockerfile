FROM sawacl/python-poetry

RUN mkdir /app
WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry install

COPY . .

ENTRYPOINT ["poetry", "run", "./manage.py", "runserver", "0.0.0.0:8000"]
