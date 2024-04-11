from fastapi import APIRouter, Depends

router = APIRouter(
    prefix='/topic',
    tags=['topic'],
)

# Create a Topic
@router.post('/create')
def create_topic():
    pass

# Read a Topic with specifc id
@router.get('/read/{id}')
def get_topic_by_id():
    pass

# Read all Topic
@router.get('/read/all')
def get_all_topic():
    pass

# Edit a Topic with specific id
@router.patch('/edit/{id}')
def edit_topic_info():
    pass

# Delete a Topic with specific id
@router.delete('/delete/{id}')
def delete_topic():
    pass