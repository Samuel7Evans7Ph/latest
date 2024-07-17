from fastapi.responses import JSONResponse
from typing import Annotated
import cv2
import os
import asyncio
import PIL

from temp import *

from PIL import Image

from check_status import *

from fastapi import FastAPI,Path,Query,Form,File,UploadFile,BackgroundTasks

app=FastAPI()
from database_update import *
from process_initialisation import *


#@app.get("/upload_file/{}")


@app.get("/upload_file")
async def check_status(image_file_name:str):
    pres_status=present_status(image_file_name)

    return{"present status":pres_status}

async def start_process(token_id:str):

#    await asyncio.sleep(10)
    image_file_name=update_database(token_id)
    initialise(image_file_name)


@app.post("/upload_file/{token_id}")
async def upload_picture (background_tasks:BackgroundTasks,token_id:str):

    background_tasks.add_task(start_process,token_id)
    return JSONResponse(status_code=200, content={"message": "Picture upload initiated"})




#@app.post("/login/")
#async def login(username:Annotated[str,Form()],password:Annotated[str,Form()]):
 #   return {"username":username}

#@app.post("/uploadfile/")
#async def create_upload_file(file:UploadFile):
#    contents=await file.read()
#    return {contents}
#


#@app.post("/upload_file/{image_file_name}")
#async def start_process(image_file_name:str):
#    update_database(image_file_name)
 #   initialise(image_file_name)



#@app.get("/upload")
#async def get_results(image_file_name:str):
#    no_of_faces=





@app.post("/upload_file")
async def send_image(image_file:UploadFile):
    contents=await image_file.read()
    
    if not os.path.isdir("Uploaded_Images"):
        os.makedirs("Uploaded_Images")
    


    with open(os.path.join("Uploaded_Images", image_file.filename), "wb") as f:
        f.write(contents)


    # meta_integrate(contents)
    unique_string=add_file_path(os.path.join("Uploaded_Images",image_file.filename))
    

    return {"token_id":unique_string}
    

    

