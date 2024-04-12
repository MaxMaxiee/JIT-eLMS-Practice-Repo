from fastapi import FastAPI
from db.database import engine
from db import models
from router import admin_router, course_router, lesson_router, topic_router, quiz_router, activity_router
from auth import authentication

app = FastAPI()

# Routers for each objects
app.include_router(admin_router.router)
app.include_router(authentication.router)
app.include_router(course_router.router)
app.include_router(lesson_router.router)
app.include_router(topic_router.router)
app.include_router(quiz_router.router)
app.include_router(activity_router.router)

@app.get('/testserver')
def index():
    return {
        'message': 'server is working'
    }

models.Base.metadata.create_all(engine)