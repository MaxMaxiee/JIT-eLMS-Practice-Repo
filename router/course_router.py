from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/course',
    tags=['course'],
)

# Create a Course
@router.post('/create')
def create_course():
    pass

# Read a Course with specific id
@router.get('/read/{id}')
def get_course_by_id():
    pass

# Read all Course
@router.get('/read/all')
def get_all_course():
    pass

# Edit a Course with specific id
@router.patch('/edit/{id}')
def edit_course_info():
    pass

# Delete a Course with specific id
@router.delete('/delete/{id}')
def delete_course():
    pass