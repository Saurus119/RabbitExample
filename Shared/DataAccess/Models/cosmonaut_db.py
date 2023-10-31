from datetime import datetime
from sqlalchemy import  Column, String, DateTime, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, class_mapper
from sqlalchemy import  String, String

Base = declarative_base()

class CosmonauntModel(Base):
    __tablename__ = "Cosmonauts"
    
    Id : Mapped[int] = mapped_column(primary_key=True)
    Name = mapped_column(CHAR(50))
    Date = Column(DateTime, default=datetime.now)

    @classmethod
    def from_validation_model(cls, validation_model):
        return CosmonauntModel(Name=validation_model.name.strip())
    
    def to_dict(self) -> dict:
        return {column.name: getattr(self, column.name) for column in class_mapper(self.__class__).mapped_table.c}