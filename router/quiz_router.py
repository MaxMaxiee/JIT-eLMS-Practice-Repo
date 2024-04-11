from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/quiz',
    tags=['quiz'],
)

# Create a Quiz
@router.post('/create')
def create_quiz():
    pass

# Read a Quiz with specific id
@router.get('/read/{id}')
def get_quiz_by_id():
    pass

# Read all Quiz
@router.get('/read/all')
def get_all_quiz():
    pass

# Edit a Quiz with specific id
@router.patch('/edit/{id}')
def edit_quiz_info():
    pass

# Delete a Quiz with specific id
@router.delete('/delete/{id}')
def delete_quiz():
    pass