from sqlalchemy import Enum


class SponsorTypeChoices( Enum):
    legal_entity = ('legal_entity', 'Yuridik shaxs')
    individual_person = ('individual_person', 'Jismoniy shaxs')


class SponsorStatusChoices( Enum):
    new = ('new', 'Yangi')
    in_moderation = ('in_moderation', 'Moderatsiyada')
    confirmed = ('confirmed', 'Tasdiqlangan')
    denied = ('denied', 'Rad qilingan')

class SponsorPaymentType( Enum):
    transfer_money = ('transfer_money', 'Pul kochirish')
    by_card = ('by_card', 'Plastik karta')
    cash = ('cash', 'Naqd pul')