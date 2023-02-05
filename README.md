# Ecommerce-Backend

Proyecto de practica realizado por **Kenneth Corrales**

Lo mas recomendable es crear un ambiente virtual para eso se debe ejecutar el siguiente comando



```sh
  $ python -m venv venv
```

Or in linux:
```sh
  $ python3 -m venv .venv
```
List of dependencies/libraries:
- dotenv python
- fastapi
- uvicorn
- kink
- pydantic


The project is organized to work with the three major parts of hexagonal architecture 

Study "cls" python  used in errors.py

To build the docker image and run the container execute the following commands

Create Image:
```sh
  $ docker image build -t backend .
```

Create Container:
```sh
  $ docker container run --publish 8001:15400 --name backend backend
```

With this the project you can call the API in the localhost:8001