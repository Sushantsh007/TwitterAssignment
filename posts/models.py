from sqlalchemy import ForeignKey, Column, Integer, text,String, CHAR, create_engine, Text, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased
from geoalchemy2 import Geometry
from geoalchemy2.functions import ST_Distance_Sphere, ST_Point
from shapely.wkb import loads
# import struct
# from flask_sqlalchemy import Pagination

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'

    id = Column("id",Integer,primary_key = True,autoincrement = True)
    message = Column("message",Text,nullable=False)
    loc = Column("loc",Geometry('POINT'),nullable=False)

    def __init__(self, message, lat,lon):
        self.message = message
        self.loc = f'POINT({lat} {lon})'

 
engine = create_engine("postgresql+psycopg2://sushant:sushant@localhost:5432/test", echo = True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

def create(message, lat, lon):
    try:
        p1 = Post(message,lat,lon)
        session.add(p1)
        session.commit()
    except:
        raise Exception("problem occured")

def get(lat, lon, page=1, per_page=10):
    try:
        point = f'POINT({lat} {lon})'
        query = session.query(Post.id, Post.message, Post.loc, func.ST_DistanceSphere(Post.loc, point).label('distance')).order_by('distance')
        posts = query.all()
        if not posts:
            return [], 0
        
        total = len(posts)
        start = (page-1)*per_page
        end = start + per_page
        posts = posts[start:end]
        
        results = []
        for row in posts:
            result = {
                'id': row[0],
                'message': row[1],
                'location': row[2],
                'distance_m': row[3]
            }
        results.append(result)
        
        return results
    except Exception as e:
        print(e)
        return "False"


