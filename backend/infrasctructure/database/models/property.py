from . import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey


class PropertyRegister(DeclarativeBase):

    __tablename__ = 'property_registers'

    class Constraints:
        NAME_MAX_VALUE = 100

    name = Column(
        String(Constraints.NAME_MAX_VALUE), unique=True, nullable=False
    )

    photos = relationship(
        "PropertyRegisterImage",
        primaryjoin="PropertyRegisterImage.property_register_id == PropertyRegister.id"
    )


class PropertyRegisterImage(DeclarativeBase):
    
    __tablename__ = 'property_registers_images'

    property_register_id = Column(
        Integer,
        ForeignKey(f'{PropertyRegister.__tablename__}.id')
    )
    filename = Column(String)
