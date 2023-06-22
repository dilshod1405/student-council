FROM python:3.9.17

WORKDIR /app

COPY . /app/

RUN pip install -r requirement.txt

EXPOSE 8000

ENTRYPOINT [ "./entrypoint.sh" ]