from sqlalchemy import Column, Integer, String

from .base_meta import Base


class Auto(Base):
    __tablename__ = "Auto"

    number_auto = Column(String, nullable=False, primary_key=True)
    id_client = Column(Integer)
    marka = Column(String)

    def __str__(self):
        return f"Auto {self.number_auto} {self.marka} {self.id_client}"
