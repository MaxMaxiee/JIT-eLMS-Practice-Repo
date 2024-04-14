# Schemas
from pydantic import BaseModel, EmailStr, Field
from typing import List
from fastapi import HTTPException, status


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