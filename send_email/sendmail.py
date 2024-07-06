import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, password, smtp_server='mail.shahibu.com', smtp_port=465, use_ssl=False, use_tls=True):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        if use_ssl:
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:
            server = smtplib.SMTP(smtp_server, smtp_port)
            if use_tls:
                server.starttls() 
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


from_email ='jobportal@shahibu.com'
password ='C@rE$Nfyo$I^'
to_email ='okumuarthur496@gmail.com'
subject ='Hello World'
body = "This is a test email sent from Python!"

send_email(subject, body, to_email, from_email, password, use_ssl=True, use_tls=False)