from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/activity',
    tags=['activity'],
)

@router.post('/create')
def create_activity():
    pass

@router.get('/read/{id}')
def get_activity_by_id():
    pass

@router.get('/read/all')
def get_all_activity():
    pass

@router.patch('/edit/{id}')
def edit_activity_info():
    pass

@router.delete('/delete')
def delete_activity():
    pass