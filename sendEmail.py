# Import the necessary modules
from email.message import EmailMessage
import ssl
import smtplib

# Gmail SMTP server settings
yourgmail = ''  # Your Gmail address
yourgmailpass = ''  # Your Gmail password
sendto = ''  # Recipient's email address

# Define the email subject and body
subject = "Python send email test"
body = """
    Hi everyone!
    I hope you are well! This is a Python program that can send an email. It's so cool and can be 
    used for many things! ☺☻
    See you soon!
"""

# Create an EmailMessage object and set its attributes
email = EmailMessage()
email['From'] = yourgmail
email['To'] = sendto
email['subject'] = subject
email.set_content(body)

# Create a SSL context
context = ssl.create_default_context()

# Connect to the Gmail SMTP server using SSL
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # Log in to your Gmail account
    smtp.login(yourgmail, yourgmailpass)
    
    # Send the email
    smtp.sendmail(yourgmail, sendto, email.as_string())
    
    # Print a success message
    print("The email was successfully sent!\n")
