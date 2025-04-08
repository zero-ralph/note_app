
from sqlalchemy import create_engine, URL, inspect
from sqlalchemy.orm import sessionmaker
from src.config.settings import Settings

from src.config.base import Base


SQLALCHEMY_DATABASE_URL = None
ENGINE = None
SESSIONLOCAL = None



def configure_database(settings: Settings):
    global SQLALCHEMY_DATABASE_URL, ENGINE, SESSIONLOCAL

        
    SQLALCHEMY_DATABASE_URL = URL.create(
        drivername="postgresql",
        username=settings.database.user,
        password=settings.database.password,
        port=settings.database.port,
        host=settings.database.host,
        database=settings.database.name
    )

    ENGINE = create_engine(SQLALCHEMY_DATABASE_URL, echo=False, pool_pre_ping=True)
    SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

    # Create all tables 
    from src.models import Note
    Base.metadata.create_all(bind=ENGINE)
    # LOG HERE

def get_db():

    db = SESSIONLOCAL()
    try:
        yield db
    finally:
        db.close()