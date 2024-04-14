# Database operations for admin
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db.models import DbAdmin, DbLogin
from schemas import AdminBase
from db.hash import Hash
from pydantic import EmailStr

def get_admin_by_email(db: Session, email: str):
    admin = db.query(DbAdmin).filter(DbAdmin.email == email).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Admin with email {email} not found')
    return admin

def create_admin(db: Session, request: AdminBase):

    # Checks if the email already exist
    if db.query(DbAdmin).filter(DbAdmin.email == request.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exist")

    # Creates an admin account
    admin = DbAdmin(
        firstname = request.firstname,
        middlename = request.middlename,
        lastname = request.lastname,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

def get_admin(db: Session, id: int):
    admin = db.query(DbAdmin).filter(DbAdmin.id == id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Admin with id {id} not found')
    return admin

def get_all_users(db: Session):
    return db.query(DbAdmin).all()

def update_admin(db: Session, id:int, request:AdminBase):
    admin = db.query(DbAdmin).filter(DbAdmin.id == id)
    if not admin.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Admin with id {id} not found')
    admin.update({
        DbAdmin.firstname: request.firstname,
        DbAdmin.middlename: request.middlename,
        DbAdmin.lastname: request.lastname,
        DbAdmin.email: request.email,
        DbAdmin.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'Admin Information Updated'

def delete_admin(db:Session, id: int):
    admin = db.query(DbAdmin).filter(DbAdmin.id == id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Admin with id {id} not found')
    db.delete(admin)
    db.commit()
    return 'Deleted'



