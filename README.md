# PyDataBCN Workshop

Este repositorio contiene scripts y documentos para el taller de PyDataBCN. "De los datos al modelo en producción"

> Comenzaremos con un conjunto de datos de imágenes sin procesar, entrenaremos
> un modelo de aprendizaje automático usando fastai/PyTorch y crearemos una
> aplicación web con FastAPI para permitir que los usuarios interactúen con el
> modelo.

**IMPORTANTE**

Los contenidos están orientados a un sistema UNIX (macOS o Linux), se puede
realizar el taller con Windows, pero es posible que haya que adaptar algunos
comandos. Puede haber algunos archivos para Windows (por ejemplo:
`requirements-windows.txt`), pero ninguno de estos ha sido probado.

## Requisitos previos

1. Para poder realizar el taller es necesario tener instalado Python 3.7 o superior.
2. Se recomienda utilizar un entorno virtual para instalar las dependencias. En el taller se usará el módulo `venv` de Python, pero
   otros gestores de entornos virtuales como `conda`/`mamba`/`micromamba` también son válidos.
3. Durante el taller se usará VSCode como editor de archivos de texto y notebooks de Jupyter. Cada asistente puede utilizar el editor que
   considere.
4. Crear un entorno virtual en instalar las dependencias antes de iniciar el taller.

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -U pip setuptools wheel
python3 -m pip install -U -r requirements.txt
```

5. Descargar los datos antes del inicio del taller (120MB). El script `download.py` se encarga de descargar los datos y descomprimirlos.

```sh
python3 download.py
```

Durante el taller entrena un modelo de clasificación de imágenes sencillo usando
[fastai](https://docs.fast.ai/). Se recomienda tener al menos 10GB de espacio
libre en el disco duro y al menos 8GB de RAM.

6. En el taller crearemos una aplicación web para utilizar nuestro modelo.
   Podremos usar la aplicación desde otros dispositivos y con una URL pública. Para
   esto es necesario instalar `cloudflared` (NO es necesario tener una cuenta en
   Cloudflare ni configurar nada). Esto es opcional, y solamente se utilizará para
   que otros participantes del taller pueda probar la aplicación.

https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/local/#1-download-and-install-cloudflared

## Sobre el taller

Todo el taller se realizará "en directo". Es decir, todo el código se escribirá
durante el taller. Cada participante tedrá libertad sobre la implementación
final del código.

Algunos graficos generados por `fastai` no funcionan correctamente en VSCode, se
puede añadir el siguiente código al principio del notebook para solucionar el
problema [[fuente](https://github.com/microsoft/vscode-jupyter/issues/13163)].

```python
from IPython.display import clear_output, DisplayHandle
def update_patch(self, obj):
    clear_output(wait=True)
    self.display(obj)
DisplayHandle.update = update_patch
```

Quizá durante el taller alguien quiere probar el modelo con imágenes hechas con
el móvil. Algunos móviles generan images en formato HEIC. Para poder trabajar
con estas imágenes, tendremos que installer la librería `pi-heif` y cargarla
antes de usar el modelo.

```sh
# activar el entorno virtual!!
python3 -m pip install pi-heif
```

```python
from pi_heif import register_heif_opener

register_heif_opener()
```

**Importante para macOS con procesadores ARM**

Pytorch intentará utilizar la GPU del sistema, pero no todas las operaciones
están soportadas. Antes de ejecutar ningún script/notebook, hay que configurar
la siguiente variable del entorno. (Importante hacerlo en el mismo
entorno/terminal donde se vayan a ejecutar los scripts/notebooks)

```sh
export PYTORCH_ENABLE_MPS_FALLBACK=1
```

## Enlaces

- FastAI: https://docs.fast.ai/
- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/latest/
- MDN `<form>`: https://developer.mozilla.org/es/docs/Web/HTML/Element/form
- sqlite3: https://docs.python.org/3/library/sqlite3.html

- https://fastapi.tiangolo.com/tutorial/request-forms/
- https://fastapi.tiangolo.com/tutorial/request-files/
- https://fastapi.tiangolo.com/tutorial/request-forms-and-files/

- https://docs.fast.ai/tutorial.imagenette.html#loading-the-data-with-the-data-block-api
- https://docs.fast.ai/data.transforms.html#split

## Meta

Ricardo Ander-Egg Aguilar – [@ricardoanderegg](https://twitter.com/ricardoanderegg) –

- [ricardoanderegg.com](http://ricardoanderegg.com/)
- [github.com/polyrand](https://github.com/polyrand/)

## Otros enlaces (no relacionados con el taller)

- https://www.robots.ox.ac.uk/~vgg/data/pets/
- https://unsplash.com/
- https://huggingface.co/models?pipeline_tag=image-classification
- https://huggingface.co/docs/transformers/main/en/model_doc/resnet
- https://huggingface.co/docs/transformers/tasks/image_classification
