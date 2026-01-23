from epl import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class Club(db.Model):
    __tablename__ = 'club'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    stadium: Mapped[str] = mapped_column(String(50), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    logo: Mapped[str] = mapped_column(String(256), nullable=False)

    players: Mapped[List["Player"]] = relationship("Player", back_populates='club')

    def __repr__(self):
        return f'<Clubs {self.name}>'

class Player(db.Model):
    __tablename__ = 'player'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    position: Mapped[str] = mapped_column(String(20), nullable=False)
    nationality: Mapped[str] = mapped_column(String(50), nullable=False)
    img: Mapped[str] = mapped_column(String(256), nullable=False)
    club_id: Mapped[int] = mapped_column(Integer, ForeignKey('club.id'), nullable=False)

    club: Mapped["Club"] = relationship("Club", back_populates='players')

    def __repr__(self):
        return f'<Players: {self.name}>'

