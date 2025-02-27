from sqlalchemy import ForeignKey, String, BigInteger, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(128))
    about: Mapped[str] = mapped_column(String(512))
    image: Mapped[str] = mapped_column(String(256))

class Item_Card(Base):
    __tablename__ = "item_cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    title: Mapped[str] = mapped_column(String(128))
    about: Mapped[str] = mapped_column(String(512))
    price: Mapped[str] = mapped_column(String(15))
    instruction: Mapped[str] = mapped_column(String(128))


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    item_card: Mapped[int] = mapped_column(ForeignKey("item_cards.id"))
    data: Mapped[str] = mapped_column(String(128))
    bought: Mapped[bool] = mapped_column(default=False)


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey("users.id"))
    item: Mapped[int] = mapped_column(ForeignKey("items.id"))
    count: Mapped[int]
