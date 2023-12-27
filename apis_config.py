from fastapi import FastAPI

description = """
Nutriary API helps you do clasiffiing indonesian foods. 🚀

## Items

You can go to /documentation for more information and how to use it.

## Users

You will be able to:

* **Send Image and Predict** (Implemented).
"""

tags_metadata = [
    {
        "name" : "predict",
        "description": "Predict an image"
    }
]

app = FastAPI(
    title="scanlori-API",
    description=description,
    version="1.0.0",
    contact={
        "name": "CH2-PS421",
        "url": "https://github.com/CH2-PS421",
        "email": "yudhiwinantoro@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/mit/",
    },
    openapi_tags=tags_metadata
)