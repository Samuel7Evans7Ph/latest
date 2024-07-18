from fastapi.responses import JSONResponse
from typing import Annotated
import cv2
import os
import asyncio
import PIL

from temp import *
from PIL import Image
from check_status import *
from fastapi import FastAPI, Path, Query, Form, File, UploadFile, BackgroundTasks

app = FastAPI()
from database_update import *
from process_initialisation import *


@app.get("/upload_file")
async def check_status(unique_string: str):
    pres_status = present_status(unique_string)

    return {"present status": pres_status}


async def start_process(token_id: str):

    image_file_name = update_database(token_id)
    initialise(image_file_name, token_id)


@app.post("/upload_file/{token_id}")
async def upload_picture(background_tasks: BackgroundTasks, token_id: str):

    background_tasks.add_task(start_process, token_id)
    return JSONResponse(
        status_code=200, content={"message": "Picture upload initiated"}
    )


@app.post("/upload_file")
async def send_image(image_file: UploadFile):
    contents = await image_file.read()

    if not os.path.isdir("Uploaded_Images"):
        os.makedirs("Uploaded_Images")

    with open(os.path.join("Uploaded_Images", image_file.filename), "wb") as f:
        f.write(contents)

    unique_string = add_file_path(os.path.join("Uploaded_Images", image_file.filename))

    return {"token_id": unique_string}
