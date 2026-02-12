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
    Index,
)
from sqlalchemy.orm import Mapped, mapped_column
from api.appdb import Base

class KSEFSessionType(Enum):
    Online = 0
    Batch = 1

class KSEFSession(Base):
    __tablename__ = "ksefsession"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)

    sesref : Mapped[str] = mapped_column(String(255), nullable=False)
    sestype: Mapped[KSEFSessionType] = mapped_column(SqlEnum(KSEFSessionType), nullable=False)
    status : Mapped[int] = mapped_column(Integer, nullable=False)
        # 0 = new
        # < 200 = waiting
        # 200 = done
        # > 300 = error
    sesdata: Mapped[str] = mapped_column(Text, nullable=True)

    idx_ksefsession_1 = Index('idx_ksefsession_1', 'sestype', 'status')

class KSEFSessionPos(Base):
    __tablename__ = "ksefsessionpos"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)

    session : Mapped[int] = mapped_column(Integer, ForeignKey("ksefsession.id"), nullable=False)
    docref : Mapped[str] = mapped_column(String(255), nullable=False)

    firma : Mapped[int] = mapped_column(Integer, ForeignKey("firma.id"), nullable=True)
    idrejvatnag : Mapped[int] = mapped_column(Integer, ForeignKey("rejvatnag.idrejvatnag"), nullable=False)
    serial : Mapped[UUID] = mapped_column(Uuid, unique=True, nullable=False)

    status : Mapped[int] = mapped_column(Integer, nullable=False)
    statusinfo : Mapped[str] = mapped_column(Text, nullable=True)

    upo: Mapped[str] = mapped_column(Text, unique=True, nullable=True)

    idx_ksefsessionpos_1 = Index('idx_ksefsessionpos_1', 'session', 'firma', 'status')
