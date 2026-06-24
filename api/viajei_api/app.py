from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import message

app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}

@app.post('/auth/', status_code=HTTPStatus.CREATED)
def login():
