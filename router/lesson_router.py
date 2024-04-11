from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/lesson',
    tags=['lesson'],
)

# Create a Lesson
@router.post('/create')
def create_lesson():
    pass

# Read a Lesson with specific id
@router.get('/read/{id}')
def get_lesson_by_id():
    pass

# Read all Lesson
@router.get('/read/all')
def get_all_lesson():
    pass

# Edit a Lesson with specific id
@router.patch('/edit/{id}')
def edit_lesson_info():
    pass

# Delete a Lesson with specific id
@router.delete('/delete/{id}')
def delete_lesson():
    pass