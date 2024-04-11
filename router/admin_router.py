from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/admin',
    tags=['admin'],
)

@router.post('/create')
def create_admin():
    pass

@router.get('/read/{id}')
def get_admin_by_id():
    pass

@router.get('/read/all')
def get_all_admin():
    pass

@router.patch('/edit/{id}')
def edit_admin_info():
    pass

@router.delete('/delete/{id}')
def delete_admin():
    pass