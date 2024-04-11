from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/admin',
    tags=['admin'],
)

# Create an Admin
@router.post('/create')
def create_admin():
    pass

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