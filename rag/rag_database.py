from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLAlchemy Base
Base = declarative_base()

# Define the Post class to map to the posts table
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    department_name = Column(String(255), nullable=False)
    notice_name = Column(String(255), nullable=False)
    writer = Column(String(255), nullable=False)
    view_count = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    content = Column(Text, nullable=False)
    title = Column(Text, nullable=False)

# Database configuration
DATABASE_URL = 'mysql+pymysql://root:dnlab2024@localhost:3306/llm'

engine = create_engine(DATABASE_URL)

# Create all tables
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)


