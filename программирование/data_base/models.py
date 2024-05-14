from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, BigInteger, func, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    '''created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())'''


class Training(Base):
    __tablename__ = 'training'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    link: Mapped[str] = mapped_column(String(150))
    sex: Mapped[str] = mapped_column(String(150))
    common_muscle_group: Mapped[str] = mapped_column(String(150))
    detailed_muscle_group: Mapped[str] = mapped_column(String(150))
    weight_loss: Mapped[str] = mapped_column(String(150))
    weight_gain: Mapped[str] = mapped_column(String(150))
    keep_shape: Mapped[str] = mapped_column(String(150))
    energy_feelins: Mapped[str] = mapped_column(String(150))


'''class Produkt(Base):
    __tablename__ = 'produkt'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    belok: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    fat: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    carbohydrate: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    kkal: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)'''

class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    belok: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    fat: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    carbohydrate: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    kkal: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)