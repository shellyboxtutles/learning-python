import smtplib
from email.mime.text import MIMEText

def send_sms_via_gmail(sender_email, sender_password, recipient_phone, carrier_gateway, message):
    # Combine the phone number and the carrier gateway
    recipient_email = f"{recipient_phone}@{carrier_gateway}"
    
    # Create a MIMEText object
    msg = MIMEText(message)
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "verification code"

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Message sent successfully!")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Replace with your Gmail credentials, phone number, and carrier gateway
send_sms_via_gmail('g.python.website.and.app.developers@gmail.com', 'hohi mkas ompn frdd', '8582695524', 'tmomail.net', 'verify')
