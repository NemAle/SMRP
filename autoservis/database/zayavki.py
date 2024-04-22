from datetime import date
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base_meta import Base

class Zayavki(Base):
    __tablename__ = "Zayavki"

    id_zayavki = Column(Integer, primary_key=True, nullable=False)
    data = Column(String(20), nullable=False)
    cena = Column(Integer, nullable=True)
    id_client = Column(Integer, ForeignKey("Client.id_client"), nullable=True)

    client = relationship("Client", back_populates="zayavk")
    zayavka_rabs = relationship("Rabotnik", back_populates="zayavka")

    def __str__(self):
        return f"Zayzvka {self.id_zayavki} {self.data} {self.cena} {self.id_rab}"

    def __repr__(self):
        return str(self)
