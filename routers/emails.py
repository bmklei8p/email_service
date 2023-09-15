from fastapi import APIRouter
from models import Email, User
from config import settings
from smtplib import SMTP
from fastapi import Depends
from queries.users import UserQueries
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from jinja2 import Environment, FileSystemLoader
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



router = APIRouter()

# def validate_user(API_KEY, email, repo: UserQueries = Depends()):
#     ## have to add a check for the API_KEY with mongodb to compare to the one in the database and the email of the user and ensure that they are the same
#     user = repo.get_one(email)
#     if (user.API_KEY == API_KEY):
#         return True
#     else:
#         return False


def validate_user(email: Email, repo: UserQueries = Depends()):
    user = repo.get_one(email.recieverEmail)
    if user and user.API_KEY == email.API_KEY:
        return True
    else:
        return False


@router.post("/submit-form")
# def submit_form(email: Email):
def submit_form(email: Email, validated_user: bool = Depends(validate_user)):
    # validatedUser = validate_user(email.API_KEY, email.recieverEmail)
    if not validated_user:
        return JSONResponse(
            content={"Message": "API_KEY or email is incorrect"}, status_code=401
        )
    template_env = Environment(loader=FileSystemLoader(os.path.abspath(".")))
    template = template_env.get_template("email_template.html")
    email_content = template.render(email=email)

    try:
        # Email configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        sender_email = settings.gmail_email
        receiver_email = email.recieverEmail
        smtp_username = settings.gmail_email
        smtp_password = settings.gmail_app_password

        # Construct the email message
        # message = f"Subject: {email.subject} from {email.senderName}\n\nComment: {email.comment} \n this comment was sent from {email.senderEmail}"


        # Send the email
        with SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            msg = MIMEMultipart()
            msg["Subject"] = email.subject
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg.attach(MIMEText(email_content, "html"))
            server.sendmail(sender_email, receiver_email, msg.as_string())
            # server.sendmail(sender_email, receiver_email, message)

        return JSONResponse(
            content={"Message": "Email sent successfully"}, status_code=201
        )

    except Exception as e:
        return JSONResponse(
            content={"Message": "Failed to send email", "error": str(e)},
            status_code=500,
        )
