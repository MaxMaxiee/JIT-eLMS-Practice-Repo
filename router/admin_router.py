from fastapi import APIRouter, Depends
from schemas import AdminDisplay, AdminBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_admin

router = APIRouter(
    prefix='/admin',
    tags=['admin'],
)

# Create an Admin
@router.post('/create', response_model=AdminDisplay)
def create_admin(request: AdminBase, db: Session = Depends(get_db)):
    return db_admin.create_admin(db, request)

# Read an Admin with specific id
@router.get('/read/{id}')
def get_admin_by_id():
    pass

# Read all Admin
@router.get('/read/all')
def get_all_admin():
    pass

# Edit an Admin Info with specific id
@router.patch('/edit/{id}')
def edit_admin_info():
    pass

# Delete an Admin with specific id
@router.delete('/delete/{id}')
def delete_admin():
    pass