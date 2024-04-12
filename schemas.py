# Schemas
from pydantic import BaseModel
from typing import List

class AdminBase(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    email: str
    password: str

class AdminDisplay(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    email: str