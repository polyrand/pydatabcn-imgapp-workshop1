import base64
import json
import sys
import uuid

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


@app.post("/test/")
async def test(request: Request, imagen_entrada: Annotated[bytes, File()]):
    prediccion = learn.predict(imagen_entrada)
    predict_id = uuid.uuid4()
    with open("result.json", "w") as f:
        f.write(
            json.dumps(
                {
                    "id": str(predict_id),
                    "prediccion": prediccion[0],
                    "bytes": base64.b64encode(imagen_entrada).decode("utf-8"),
                }
            )
        )
    print(prediccion[0])
    return templates.TemplateResponse(
        "response.html.j2",
        {"request": request, "prediccion": prediccion[0], "pred_id": predict_id},
    )


@app.get("/feedback")
def feedback(request: Request, texto_feebdack: str, ident: str):
    print(ident, texto_feebdack)
    return "ok"


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
