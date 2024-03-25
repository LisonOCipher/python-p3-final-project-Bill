from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Create tables
class Customers(Base):
    __tablename__ = 'customers'
    name = Column(VARCHAR, primary_key=True)
    age = Column(Integer)
    email = Column(VARCHAR)
    address = Column(VARCHAR)

class Pieces(Base):
    __tablename__ = 'pieces'
    piece_name = Column(VARCHAR, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    category_of_piece = Column(VARCHAR)
    price = Column(Integer)
    

class Companies(Base):
    __tablename__ = 'companies'
    company_name = Column(VARCHAR, primary_key=True)
    location = Column(VARCHAR)
    established_year = Column(Integer)
    

class Comment(Base):
    __tablename__ = 'comments'
    comment_text = Column(VARCHAR, primary_key=True)
    piece_name = Column(VARCHAR, ForeignKey('pieces.piece_name'))

engine = create_engine('sqlite:///art_gallery.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()