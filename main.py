from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from smtplib import SMTP
import os

# # local
# from functools import lru_cache

# #prod
from config import settings
#local
# from config import Settings
# from typing_extensions import Annotated


app = FastAPI()

origins = [
    os.environ.get("CORS_HOST", "http://localhost"),
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Email(BaseModel):
    name: str
    email: str
    subject: str
    comment: str

# local
# @lru_cache()
# def get_settings():
#     return Settings()


# local
# def submit_form(email: Email, settings: Settings = Depends(get_settings)):
# deployed
@app.get("/list-routes")
def get_all_urls():
    url_list = [{"path": route.path, "name": route.name} for route in app.routes]
    return url_list

@app.get("/")
def get_works():
    return {"Message": "This should work"}

@app.post("/submit-form")
def submit_form(email: Email):
    try:
        # Email configuration

        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        # sender_email = settings.gmail_email
        # receiver_email = settings.reciever_email
        # smtp_username = settings.gmail_email
        # smtp_password = settings.gmail_app_password

        sender_email = "kleinbergbryan@gmail.com"
        receiver_email = "bmklei8p@gmail.com"
        smtp_username = "kleinbergbryan@gmail.com"
        smtp_password = "onarkreneyeihqcd"

        # Construct the email message
        message = f"Subject: {email.subject} from {email.name}\n\nComment: {email.comment} \n this comment was sent from {email.email}"

        # Send the email
        with SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message)

        return {"message": "Email sent successfully"}

    except Exception as e:
        return {"message": "Failed to send email", "error": str(e)}