from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/quiz',
    tags=['quiz'],
)

@router.post('/create')
def create_quiz():
    pass

@router.get('/read/{id}')
def get_quiz_by_id():
    pass

@router.get('/read/all')
def get_all_quiz():
    pass

@router.patch('/edit/{id}')
def edit_quiz_info():
    pass

@router.delete('/delete/{id}')
def delete_quiz():
    pass