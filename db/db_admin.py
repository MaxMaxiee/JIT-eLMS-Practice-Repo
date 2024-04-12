# Database operations for admin
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