"""
Courtesy of samlopezf on Github: https://github.com/samlopezf/Python-Email/blob/master/send_email.py

"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib

def Notify(openSeats, email, password):
    
    fromEmail = email # sender's email address
    emailPass = password # sender's email password
    toEmail = email # recipient's email address

    subject = 'Seat Change' 
    
    message = 'Huzzah! ' + openSeats + ' open seat(s) found!'

    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = subject


    msg.attach(MIMEText(message, 'plain'))

    filename = 'OpenCourse.png'
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " +filename)

    msg.attach(part)

    text = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromEmail,emailPass)
    server.sendmail(fromEmail, toEmail, text)
    server.quit()