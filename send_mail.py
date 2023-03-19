import csv
import email
from email import message
from email.quoprimime import quote 
import smtplib
from email.message import EmailMessage

#method to get admin's SMTP server credentials 
def get_credentials(filepath):
    #allowing read of credentials.txt 
    with open("credentials.txt", "r") as f:
        email_address = f.readline()
        email_password = f.readline()
    return (email_address, email_password)

#method to login into host's SMTP mail server
def login(email_address, email_password, l):
    #identify domain name of sending host to SMTP
    l.ehlo()
    #start TLS for security
    l.starttls()
    l.ehlo()
    #Authentication
    l.login(email_address, email_password)
    print("login")


#method for automated mailing service
def send_mail():
    s = smtplib.SMTP("smtp.gmail.com",587)
    email_address, email_password = get_credentials("./credentials.txt")
    login(email_address, email_password, s)

    #Message
    subject = "Welcome to Automated Email Sender"
    body = """Automated email sender service used to send emails to recipient from a csv file\n Thank you!"""

    message = EmailMessage()
    message['Subject'] = subject 
    message.set_content(body)
    
    with open("emails.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        for email in spamreader:
            s.send_message(email_address, email[0], message)
            print("Send to " + email[0])

    s.quit()
    print("Sent")



# Main
if __name__ == "__main__":
    send_mail()
    


