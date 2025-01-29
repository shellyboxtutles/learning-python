from random import randint
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

path1 = randint(1, 9)
path2 = randint(1, 9)
path3 = randint(1, 9)
path4 = randint(1, 9)
path5 = randint(1, 9)
path6 = randint(1, 9)
# Email credentials
sender_email = "g.python.website.and.app.developers@gmail.com"
receiver_email = input("enter your gmail: ")
password = "hohi mkas ompn frdd"

var1 = f"{path1}{path2}{path3} {path4}{path5}{path6}"
# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = f"{receiver_email}"
message["Subject"] = "verification code"
body = f"your verification code is: \n{var1}\nif you have not reqested a verification code, please contact g.python.website.and.app.developers@gmail.com. thank you"
message.attach(MIMEText(body, "plain"))

# Connect to Gmail's SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    # Log in to your email account
    server.login("g.python.website.and.app.developers@gmail.com", password)
    
    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Terminate the SMTP session
    server.quit()

def verify():
    var1.strip()
    var3 = input("enter verification code: ")
    if var3==var1: print("correct")
    else: print("incorect verification code. \ntry again"), verify()
verify()