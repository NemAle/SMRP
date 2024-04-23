from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DB_HOST, DB_PORT, DB_PASSWORD, DB_USER, DB_NAME

Base = declarative_base()
# engine = create_engine("sqlite:///../AutoServis.db", echo=False)
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=False)
get_session = sessionmaker(engine, autocommit=False)
