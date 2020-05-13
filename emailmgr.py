import smtplib

def send_email(rec_email,name,passcode):
    sender_email = "mgrpwd56@gmail.com"
    password = "pwd@1234"
    message="Hello {},your passcode for Password Manager is {} ".format(name,passcode)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, rec_email, message)
    return "OK"
 