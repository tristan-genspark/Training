# use a node base image
FROM python:2.7

COPY microhttp.py ./app/
WORKDIR /app

CMD [ "python", "./microhttp.py" ]

# tell docker what port to expose
EXPOSE 80
