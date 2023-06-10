import sys

import uvicorn
from fastai.vision.all import *
from fastapi import FastAPI
from fastapi import File
from fastapi import Form
from fastapi import Request
from fastapi import UploadFile
from fastapi.templating import Jinja2Templates
from typing_extensions import Annotated

app = FastAPI()

templates = Jinja2Templates(directory="templates")


def get_x(x):
    return 1


def get_y(x):
    return 1


sys.modules["__main__"].get_x = get_x
sys.modules["__main__"].get_y = get_y


learn = load_learner("test.pkl")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html.j2", {"request": request})


@app.post("/test")
async def test(request: Request, imagen_entrada: Annotated[bytes, File()]):
    print(imagen_entrada)
    return templates.TemplateResponse(
        "response.html.j2", {"request": request, "name": imagen_entrada}
    )


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
