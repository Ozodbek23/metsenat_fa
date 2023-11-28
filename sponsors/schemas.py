from pydantic import BaseModel


class SponsorSchema(BaseModel):
    id: int
    full_name: str
    phone_number: str

    class Config:
        from_attributes = True


class SponsorCreate(BaseModel):
    full_name: str
    type: # str
    phone_number: str
    status: str
    organization: str
    payment_amount: int
    # payment_type: str


class SponsorDetail(BaseModel):
    id: int
    full_name: str
    type: str
    phone_number: str
    status: str
    organization: str
    payment_amount: int
    payment_type: str
