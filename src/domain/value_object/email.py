from pydantic import BaseModel, EmailStr

class Email(BaseModel):
    adress: EmailStr

    def domain(self) -> str:
       return self.adress.split("@")[1]