from sqlalchemy.sql.schema import ForeignKey
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.orm import relationship

class DbAdmin():
    __tablename__ = 'admin'
    id = Column(String, primary_key=True)
    firsname = Column(String)
    middlename = Column(String)
    lastname = Column(String)
    email = Column(String)
    password = Column(String)

class DbCourse():
    __tablename__ = 'course'
    id = Column(String, primary_key=True)
    course_name = Column(String)
    description = Column(String)
    lesson = relationship("DbLesson", back_populates='course')

class DbLesson():
    __tablename__ = 'lesson'
    id = Column(String, primary_key=True)
    course_id = Column(String, ForeignKey('course.id'))
    title = Column(String)
    course = relationship("DbCourse", back_populates='lesson')


class DbTopic():
    __tablename__ = 'topic'
    id = Column(String, primary_key=True)
    lesson_id = Column(String, ForeignKey('lesson.id'))
    title = Column(String)
    file_url = Column(String)
    content = Column(String)
    external_link_vid = Column(String)
    external_link_mat = Column(String)

class DbActivity():
    __tablename__ = 'activity'
    id = Column(String, primary_key=True)
    activity_name = Column(String)
    content = Column(String)
    img_file_url = Column(String)
    remarks = Column(String)

class DbQuiz():
    __tablename__ = 'quiz'
    id = Column(String, primary_key=True)
    quiz_name = Column(String)

class DbQuizQuestions():
    __tablename__ = 'quiz_questions'
    id = Column(String, primary_key=True)
    quiz_id = Column(String, ForeignKey('quiz.id'))
    question_name = Column(String)

class DbQuizChoices():
    __tablename__ = 'quiz_choices'
    questions_id = Column(String, ForeignKey('quiz_questions.id'))
    choice = Column(String)


