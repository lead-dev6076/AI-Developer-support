from fastapi import FastAPI, HTTPException , Body, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional

from .embedd import work_check
from .dataextractor import createDataset

app = FastAPI()

# Mock database (a list of items)


# 1. Create an item (POST)
@app.post("/items/")
def create_item():
    w_ob = work_check()
    w_ob.working_func()
    return {"message": "everything working fine now"}
    


# 3. Read all items (GET)
@app.post("/items2/")
def read_items(command: str = Form(...),        
    text: str = Form(...),           
    channel_id: str = Form(...),    
    user_id: str = Form(...)):
    wor = work_check()
    print(text, "item")
    cont = wor.chat_func(text)
    print(cont, "what is coming")
    if cont:
        return JSONResponse({
        "response_type": "in_channel",
        "text": f"Hello, <@{user_id}>! {cont[0]}"
    })
    else:
        return {"message": ""}


# 3. Read all items (GET)
@app.get("/items1")
def get_all_items():
    data_dict = createDataset()
    return data_dict
