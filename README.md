# pythonSenderEmail
This Python script demonstrates how to send an email using Gmail's SMTP server. It creates and sends an email with a specified subject and body content to a recipient. 

To use this script, you need to provide your Gmail address, Gmail password, and the recipient's email address. 

The script uses the `EmailMessage` class from the `email.message` module to construct the email message with the specified sender, recipient, subject, and body. It then establishes a secure connection to Gmail's SMTP server using SSL with the `smtplib.SMTP_SSL()` function and logs in to your Gmail account using your credentials. 

Once authenticated, the script sends the email using the `sendmail()` method of the SMTP connection object. After the email is successfully sent, it prints a confirmation message.

This script can be useful for automating email notifications or sending messages from Python applications. Please ensure that you use it responsibly and protect your Gmail credentials.
