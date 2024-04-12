# Database operations for admin
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db.models import DbAdmin
from schemas import AdminBase
from db.hash import Hash

def create_admin(db: Session, request: AdminBase):
    new_admin = DbAdmin(
        firstname = request.firstname,
        middlename = request.middlename,
        lastname = request.lastname,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

def get_admin_by_email(db: Session, email: str):
    user = db.query(DbAdmin).filter(DbAdmin.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {email} not found')
    return user