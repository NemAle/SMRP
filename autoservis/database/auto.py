from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class Auto(Base):
    __tablename__ = "Auto"

    number_auto = Column(String(7), nullable=False, primary_key=True)
    id_client = Column(Integer, ForeignKey("Client.id_client"), nullable=False)
    marka = Column(String(50), nullable=False)

    client = relationship("Client", back_populates="auto")
    def __str__(self):
        return f"Auto {self.number_auto} {self.marka} {self.id_client}"

    def __repr__(self):
        return str(self)
