# Email-service: 

What does it do? 
This project serves as a backend server to facilitate a front-end form to be submitted to this service and it sends an email to my e-mail with all information present in the form.

## What frameworks and libraries does it utilize? 
The project was written in Python with FastAPI serving as the framework. It utilizes smtplib as a library to send the email using the smtp protocol. 

## Hurdles and resolving actions: 
1- Two factor authentication(2fa) for gmail was causing no errors and 200 status code but no mail to be sent.
1- After realizing 2fa was enabled on my gmail account, set up an app password on gmail and used instead of my standard password.

2- Message format was sending through a subject line but no other information.
2- Tried to look up documentation for the message format on the smtplib library but was unsucessful. Found solution (/n/n instead of just /n) on https://stackoverflow.com/questions/21639321/how-to-send-a-properly-formatted-email-using-python-and-smtp.

3- CORS block when sent from localhost:3000 to deployed backend.
3- Added/removed multiple configurations of localhost:3000 without success. Looked up cors documentation on fastapi and was presented with "*" wildcard option that allows all origins. 
Attempted multiple times to avoid this option due to security, but was the only successful option.
Will attempt again when front-end that uses this service is deployed to test front-end origin.