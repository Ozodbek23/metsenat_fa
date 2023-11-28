from pydantic import BaseModel


class StudentSchema(BaseModel):
    id: int
    full_name: str
    phone_number: str
    # type: str
    institute: int
    contract_amount: int

    class Config:
        from_attributes = True

class InstituteSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
class StudentCreateSchema(BaseModel):
    full_name: str
    phone_number: str
    # type: # str
    institute: int
    contract_amount: int

class StudentDetailSchema(BaseModel):
    class InstituteSchema(BaseModel):
        id: int
        name: str

    id: int
    full_name: str
    phone_number: str
    type:  str
    institutes: InstituteSchema
    contract_amount: int

    class Config:
        from_attributes = True

