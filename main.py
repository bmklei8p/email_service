from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from smtplib import SMTP


app = FastAPI()

origins = [
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


@app.post("/submit-form")
def submit_form(email: Email):
    try:
        # Email configuration
        sender_email = "kleinbergbryan@gmail.com"
        receiver_email = "bmklei8p@gmail.com"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
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


# test