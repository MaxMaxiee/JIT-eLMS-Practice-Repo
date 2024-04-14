from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from schemas import AdminDisplay, AdminBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_admin
from auth.oauth2 import get_current_user
from re import fullmatch

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

router = APIRouter(
    prefix='/admin',
    tags=['admin'],
)

def check_email(email):
    if not fullmatch(regex, email):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid Email")

# Create an Admin
@router.post('/create', response_model=AdminDisplay)
def create_admin(request: AdminBase, db: Session = Depends(get_db)):

    check_email(request.email)

    return db_admin.create_admin(db, request)

# Read an Admin with specific id
@router.get('/read/{id}', response_model=AdminDisplay)
def get_admin_by_id(id:str, db: Session = Depends(get_db), current_user: AdminBase = Depends(get_current_user)):
    return db_admin.get_admin(db, id)

# Read all Admin
@router.get('/read', response_model=List[AdminDisplay])
def get_all_users(db: Session = Depends(get_db), current_user: AdminBase = Depends(get_current_user)):
    return db_admin.get_all_users(db)

# Edit an Admin Info with specific id
@router.patch('/edit/{id}')
def edit_admin_info(id: str, request: AdminBase, db: Session = Depends(get_db), current_user: AdminBase = Depends(get_current_user)):
    check_email(request.email)
    return db_admin.update_admin(db, id, request)

# Delete an Admin with specific id
@router.delete('/delete/{id}')
def delete_admin(id: str, db: Session = Depends(get_db), current_user: AdminBase = Depends(get_current_user)):
    return db_admin.delete_admin(db, id)