from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/lesson',
    tags=['lesson'],
)

@router.post('/create')
def create_lesson():
    pass

@router.get('/read/{id}')
def get_lesson_by_id():
    pass

@router.get('/read/all')
def get_all_lesson():
    pass

@router.patch('/edit/{id}')
def edit_lesson_info():
    pass

@router.delete('/delete')
def delete_lesson():
    pass