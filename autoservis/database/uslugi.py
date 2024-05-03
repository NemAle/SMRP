from sqlalchemy import Column, Integer, String, ForeignKey
from .base_meta import Base
from sqlalchemy.orm import relationship

class Uslugi(Base):
    __tablename__ = "Uslugi"

    id_uslugi = Column(Integer, primary_key=True, nullable=False)
    remont = Column(String(50), nullable=False)
    cena = Column(Integer, nullable=True)


    usluga_rabs = relationship("Rabotnik", back_populates="usluga")

    def __str__(self):
        return f"Usluga {self.id_uslugi} {self.remont} {self.id_rab}"

    def __repr__(self):
        return str(self)
