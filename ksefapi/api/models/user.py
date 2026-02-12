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


class User(Base):
    __tablename__ = "user"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)

    imie     : Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    nazwisko : Mapped[str] = mapped_column(String(255), nullable=False)
    pesel    : Mapped[str] = mapped_column(String(255), nullable=False)

    usercert: Mapped[str] = mapped_column(Text, nullable=True)
    userkey: Mapped[str] = mapped_column(Text, nullable=True)
    userpass: Mapped[str] = mapped_column(String(255), nullable=True)

    idx_user_pesel = Index('idx_user_pesel', 'pesel')
