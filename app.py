import sqlalchemy

#Conecting to the database
engine = sqlalchemy.create_engine('mysql+pymysql://root@localhost/school', echo=True)

#mapping 
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String #facilitar a vida
Base = declarative_base()
class User(Base):
    __tablename__ = 'users' #obrigatório
    id = Column(Integer, primary_key=True) #obrigatório
    name = Column(String(50))
    fullname = Column(String(50))
    age = Column(Integer)
def __repr__(self):
    return "<User(name={}, fullname={}, age={}>".format(self.name, self.fullname, self.age)   

#Creating the table    
Base.metadata.create_all(engine)

#Adding a data
user = User(name='Enzo', fullname='Francisco Enzo', age=20)

#session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

#Adding objects
session.add(user)
session.commit()
session.add_all([
    User(name='Matheus', fullname='Matheus Silva', age=22),
    User(name='Carlos', fullname='Carlos Henrique', age=20)
])
session.commit()


