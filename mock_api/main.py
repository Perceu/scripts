from fastapi import FastAPI
from faker import Faker

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/names")
def read_names():
    fake = Faker()

    names = list()
    for i in range(10):
        names.append({"name": fake.name()})
    return names
