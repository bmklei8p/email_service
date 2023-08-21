from fastapi import APIRouter
from models import Email
from config import settings
from smtplib import SMTP

router = APIRouter()

@router.post("/submit-form")
def submit_form(email: Email):
    ## have to add a check for the API_KEY with mongodb to compare to the one in the database and the email of the user and ensure that they are the same


    try:
        # Email configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        sender_email = settings.gmail_email
        receiver_email = email.recieverEmail
        smtp_username = settings.gmail_email
        smtp_password = settings.gmail_app_password

        # Construct the email message
        message = f"Subject: {email.subject} from {email.senderName}\n\nComment: {email.comment} \n this comment was sent from {email.senderEmail}"

        # Send the email
        with SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message)

        return {"message": "Email sent successfully"}

    except Exception as e:
        return {"message": "Failed to send email", "error": str(e)}