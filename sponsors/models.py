from sqlalchemy import Column, Integer, String, Enum, BigInteger

from config.database import Base
from sponsors.choices import SponsorTypeChoices, SponsorStatusChoices, SponsorPaymentType


class Sponsors(Base):
    __tablename__ = 'sponsors'

    id = Column(Integer , primary_key=True , index=True, autoincrement=True)
    full_name = Column(String(length=125), index=True)
    # type = Column(Enum(*[choice.value for choice in SponsorTypeChoices]))
    phone_number = Column(String(length=13))
    # status = Column(Enum(*[choice.value for choice in SponsorStatusChoices]))
    # organization = Column(String(length=125), nullable=False)
    payment_amount = Column(BigInteger, default=0)
    # payment_type = Column(Enum(*[choice.value for choice in SponsorPaymentType]))


    def __str__(self):
        return f'{self.full_name}'