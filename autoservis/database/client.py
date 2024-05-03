from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_meta import Base

class Client(Base):
    __tablename__ = "Client"

    id_client = Column(Integer, primary_key=True, autoincrement=True)
    full_name_cl = Column(String(250), nullable=False)
    telephone = Column(String(15), nullable=False)

    zayavk = relationship("Zayavki", back_populates="client")
    auto = relationship("Auto", back_populates="client", uselist=False)
    def __str__(self):
        return f"Client {self.id_client} {self.full_name} {self.telephone}"

    def __repr__(self):
        return str(self)

