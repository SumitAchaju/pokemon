from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, Relationship

from database.base import Base


class Type(Base):
    __tablename__ = "type"

    name: Mapped[str] = mapped_column(unique=True)


# association table for pokemon and type many to many relationship
class PokemonType(Base):
    __tablename__ = "pokemon_type"

    type_id: Mapped[int] = mapped_column(ForeignKey("type.id", ondelete="CASCADE"))
    pokemon_id: Mapped[int] = mapped_column(
        ForeignKey("pokemon.id", ondelete="CASCADE")
    )


class Images(Base):
    __tablename__ = "images"

    back_default: Mapped[str] = mapped_column(nullable=True)
    back_female: Mapped[str] = mapped_column(nullable=True)
    pokemon_id: Mapped[int] = mapped_column(
        ForeignKey("pokemon.id", ondelete="CASCADE")
    )


class Pokemon(Base):
    __tablename__ = "pokemon"

    name: Mapped[str] = mapped_column(unique=True)
    types: Mapped[list["Type"]] = Relationship(
        secondary="pokemon_type",
        lazy="joined",
    )
    images: Mapped["Images"] = Relationship(lazy="joined")
