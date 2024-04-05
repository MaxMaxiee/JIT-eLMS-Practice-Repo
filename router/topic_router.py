from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/topic',
    tags=['topic'],
)

@router.post('/create')
def create_topic():
    pass

@router.get('/read/{id}')
def get_topic_by_id():
    pass

@router.get('/read/all')
def get_all_topic():
    pass

@router.patch('/edit/{id}')
def edit_topic_info():
    pass

@router.delete('/delete')
def delete_topic():
    pass