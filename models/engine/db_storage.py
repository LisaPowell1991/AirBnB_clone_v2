#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """
    This class creates tables in a MySQL database using SQLAlchemy.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a new instance of the DBStorage class.

        It creates a connection to the MySQL database based on the
        environmental variables and sets up the SQLAlchemy engine.
        """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    user, passwd, host, db), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of objects based on the optional class filter.

        Args:
        - cls (class): Optional. If provided, returns a filtered dictionary
          containing only instances of the specified class.

        Returns:
        - dict: A dictionary of objects or a filtered dictionary based on cls
        """
        from models import storage

        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for cls in classes:
                query = self.__session.query(cls)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """
        add a new element in the table.
        
        Args:
        - obj: An instance of a model class to be added to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits changes to the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete an element in the table

        Args:
        - obj: Optional. If provided, deletes the specified object.

        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Configures the database by creating all tables and setting up
        a new session with the SQLAlchemy engine.
        """
        from models import storage

        if self.__session is not None:
            self.__session.commit()

        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ Closes the current database session. """
        self.__session.close()
