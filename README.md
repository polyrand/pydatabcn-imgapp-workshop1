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

5. Descargar los datos antes del inicio del taller (90MB). El script `download.py` se encarga de descargar los datos y descomprimirlos.
   **La URL estará disponible en las próximas horas.**

```sh
python3 download.py <URL>
```

Durante el taller entrena un modelo de clasificación de imágenes sencillo usando
[fastai](https://docs.fast.ai/). Se recomienda tener al menos 10GB de espacio
libre en el disco duro y al menos 4GB de RAM.

## Sobre el taller

Todo el taller se realizará "en directo". Es decir, todo el código se escribirá
durante el taller. Cada participante tedrá libertad sobre la implementación
final del código.

## Enlaces

- FastAI: https://docs.fast.ai/
- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/latest/
- MDN `<form>`: https://developer.mozilla.org/es/docs/Web/HTML/Element/form
- sqlite3: https://docs.python.org/3/library/sqlite3.html

- https://docs.fast.ai/tutorial.imagenette.html#loading-the-data-with-the-data-block-api
- https://docs.fast.ai/data.transforms.html#split

## Meta

Ricardo Ander-Egg Aguilar – [@ricardoanderegg](https://twitter.com/ricardoanderegg) –

- [ricardoanderegg.com](http://ricardoanderegg.com/)
- [github.com/polyrand](https://github.com/polyrand/)

## Otros enlaces (no relacionados con el taller)

- https://huggingface.co/models?pipeline_tag=image-classification
- https://huggingface.co/docs/transformers/main/en/model_doc/resnet
- https://huggingface.co/docs/transformers/tasks/image_classification
