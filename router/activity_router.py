from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/activity',
    tags=['activity'],
)

# Create an Activity
@router.post('/create')
def create_activity():
    pass

# Read an Activity with specific id
@router.get('/read/{id}')
def get_activity_by_id():
    pass

# Read all Activity
@router.get('/read/all')
def get_all_activity():
    pass

# Edit an Activity with specific id
@router.patch('/edit/{id}')
def edit_activity_info():
    pass

# Delete an activity with specific id
@router.delete('/delete/{id}')
def delete_activity():
    pass