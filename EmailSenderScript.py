import smtplib
from email.message import EmailMessage
from getpass import getpass

def create_email():
    # CLI-GUI
    sender = input("Enter your email address: ")
    recipient = input("Enter recipient emails (comma-separated): ")
    subject = input("Enter the subject of your email: ")
    body = input("Enter the body of your email: \n")
    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    send_email(sender, msg)

def send_email(sender, msg):
    password = getpass(f"Enter {sender}'s password: ")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your app password.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        server.quit()

def main():
    create_email()

if __name__ == "__main__":
    main()