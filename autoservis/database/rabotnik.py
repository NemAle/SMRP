from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base_meta import Base


class Rabotnik(Base):
    __tablename__ = "Rabotnik"

    id_uslugi = Column(Integer, ForeignKey("Uslugi.id_uslugi"), primary_key=True, nullable=False)
    id_zayavki = Column(Integer, ForeignKey("Zayavki.id_zayavki"), primary_key=True, nullable=False)
    full_name_rab = Column(String(250), nullable=False)
    post = Column(String(25), nullable=False)

    usluga = relationship("Uslugi", back_populates="usluga_rabs")
    zayavka = relationship("Zayavki", back_populates="zayavka_rabs")

    def __str__(self):
        return f"Rabotnik {self.id_rab} {self.full_name_rab} {self.post}"

    def __repr__(self):
        return str(self)
