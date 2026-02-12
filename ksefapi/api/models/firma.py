from datetime import datetime
from uuid import UUID
from sqlalchemy import (
    Boolean,
    Integer,
    DateTime,
    Uuid,
    String,
    Text,
    #
    Index,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column
from api.appdb import Base


class Firma(Base):
    __tablename__ = "firma"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)

    nip      : Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    nazwa    : Mapped[str] = mapped_column(String(255), nullable=False)
    adres    : Mapped[str] = mapped_column(String(255), nullable=False)

    token    : Mapped[str] = mapped_column(String(255), nullable=True)

    firmacert: Mapped[str] = mapped_column(Text, nullable=True)
    firmakey: Mapped[str] = mapped_column(Text, nullable=True)
    firmapass: Mapped[str] = mapped_column(String(255), nullable=True)

    idx_firma_nip = Index('idx_firma_nip', 'nip')
