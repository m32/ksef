from uuid import UUID
from datetime import datetime
from enum import Enum
from sqlalchemy import (
    Boolean,
    Integer,
    DateTime,
    Uuid,
    String,
    Text,
    Enum as SqlEnum,
    Float,
    Time,
    #
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column
from api.appdb import Base

class KSEFStatus(Enum):
    Inserted = 0
    Closed = 1
    Send = 2

class RejVatNag(Base):
    __tablename__ = "rejvatnag"

    idrejvatnag : Mapped[int] = mapped_column(Integer, primary_key=True)
    serial : Mapped[UUID] = mapped_column(Uuid, unique=True, nullable=True)

    firma : Mapped[int] = mapped_column(Integer, ForeignKey("firma.id"), nullable=True)
    status : Mapped[KSEFStatus] = mapped_column(SqlEnum(KSEFStatus), nullable=True)
