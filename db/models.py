from sqlalchemy.sql.schema import ForeignKey
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.orm import relationship
from uuid import uuid4

# NOT FINAL MODEL

# Table for Admin
class DbAdmin(Base):
    __tablename__ = 'admin'
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    firstname = Column(String)
    middlename = Column(String)
    lastname = Column(String)
    email = Column(String)
    password = Column(String)

# Table for Login
class DbLogin(Base):
    __tablename__ = 'login'
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    email = Column(String)
    token = Column(String)

# Table for Course
class DbCourse(Base):
    __tablename__ = 'course'
    id = Column(String, primary_key=True)
    course_name = Column(String)
    description = Column(String)
    lesson = relationship("DbLesson", back_populates='course')

# Table for Lesson
class DbLesson(Base):
    __tablename__ = 'lesson'
    id = Column(String, primary_key=True)
    course_id = Column(String, ForeignKey('course.id'))
    title = Column(String)
    course = relationship("DbCourse", back_populates='lesson')

# Table for Topic
class DbTopic(Base):
    __tablename__ = 'topic'
    id = Column(String, primary_key=True)
    lesson_id = Column(String, ForeignKey('lesson.id'))
    title = Column(String)
    file_url = Column(String)
    content = Column(String)
    external_link_vid = Column(String)
    external_link_mat = Column(String)

# Table for Activity
class DbActivity(Base):
    __tablename__ = 'activity'
    id = Column(String, primary_key=True)
    activity_name = Column(String)
    content = Column(String)
    img_file_url = Column(String)
    remarks = Column(String)

# Table for Quiz
class DbQuiz(Base):
    __tablename__ = 'quiz'
    id = Column(String, primary_key=True)
    quiz_name = Column(String)

# Table for QuizQuestions
class DbQuizQuestions(Base):
    __tablename__ = 'quiz_questions'
    id = Column(String, primary_key=True)
    quiz_id = Column(String, ForeignKey('quiz.id'))
    question_name = Column(String)

# Table for QuizChoices
class DbQuizChoices(Base):
    __tablename__ = 'quiz_choices'
    questions_id = Column(String, ForeignKey('quiz_questions.id'))
    id = Column(String, primary_key=True)
    choice = Column(String)


