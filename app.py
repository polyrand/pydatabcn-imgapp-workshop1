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


# This is a small "hack" to make the load_learner work. fastai uses pickle, and
# the `learner` object includes the dataloader object. This is so that it can
# load "arbitrary" data from the dataloader without having to worry about the
# format/transformations/tensor size, etc. However, the dataloaders have a
# reference to the `get_x` and `get_y` functions. So, when it's unpickled, it
# will try to find those functions in the current scope. We don't really need
# them for inference, so a quick-fix can be defining them here, they don't have
# to do anything useful.
def get_x(x):
    return 1


def get_y(x):
    return 1


# The second part of this "hack" is a bit more... "hacky". `uvicorn` and other
# similar packages work differently with the `__main__` module in Python. So, we
# need to make sure that the `get_x` and `get_y` functions are available in the
# `__main__` module. Because even if they're defined in the global scope, when
# running this script with `uvicorn`, `__main__` will be something else.
sys.modules["__main__"].get_x = get_x
sys.modules["__main__"].get_y = get_y


learn = load_learner("test.pkl")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html.j2", {"request": request})


# TODO: Replace `File()` with UploadFile:
# https://fastapi.tiangolo.com/tutorial/request-files/?h=uploadfi#file-parameters-with-uploadfile
@app.post("/test/")
async def test(request: Request, imagen_entrada: Annotated[bytes, File()]):
    prediccion = learn.predict(imagen_entrada)
    predict_id = str(uuid.uuid4())
    # Save prediction to file, this can be reused later to re-train the model based
    # on user feedback.
    with open(f"result-{predict_id}.json", "w") as f:
        f.write(
            json.dumps(
                {
                    "id": predict_id,
                    "prediccion": prediccion[0],
                    "bytes": base64.b64encode(imagen_entrada).decode("utf-8"),
                }
            )
        )
    return templates.TemplateResponse(
        "response.html.j2",
        {"request": request, "prediccion": prediccion[0], "pred_id": predict_id},
    )


@app.get("/feedback")
def feedback(request: Request, texto_feebdack: str, identificador_interno: str):
    # Aquí ya decidimos como user el `identificador_interno` y el
    # `texto_feebdack` para generar un dataset nuevo y re-entrenar el modelo.
    print(identificador_interno, texto_feebdack)
    return "ok"


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
