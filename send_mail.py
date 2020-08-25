import smtplib
from email.mime.text import MIMEText # Allows sending of text and html emails

def send_mail(customer, developer, rating, comments):
    port = 2525 # Check with email client for what ports are allowed - In this case, it's 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '9d2603081895a4' # Use mailtrap login
    password = 'feb09f9642c757' # Use mailtrap password
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Developer: {developer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    
    sender_email = 'email1@example.com' # Placeholder - use with real domain name
    receiver_email = 'email2@examle.com' # Placeholder - use with real domain name
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Developer Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())