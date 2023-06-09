import uvicorn
from fastapi import FastAPI
from fastapi import Form
from fastapi import Request
from fastapi.templating import Jinja2Templates
from typing_extensions import Annotated

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html.j2", {"request": request})


@app.get("/test")
async def test(request: Request, name: str):
    return templates.TemplateResponse(
        "response.html.j2", {"request": request, "name": name}
    )


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
