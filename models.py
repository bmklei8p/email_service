from pydantic import BaseModel


class Email(BaseModel):
    senderName: str
    senderEmail: str
    subject: str
    comment: str
    recieverEmail: str
    API_KEY: str

class User(BaseModel):
    email: str
    API_KEY: str