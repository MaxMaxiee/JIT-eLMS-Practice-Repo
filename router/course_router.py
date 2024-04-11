from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/course',
    tags=['course'],
)

@router.post('/create')
def create_course():
    pass

@router.get('/read/{id}')
def get_course_by_id():
    pass

@router.get('/read/all')
def get_all_course():
    pass

@router.patch('/edit/{id}')
def edit_course_info():
    pass

@router.delete('/delete/{id}')
def delete_course():
    pass