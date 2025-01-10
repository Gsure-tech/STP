import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "abdulganiyu9023@gmail.com"
    password="pgno dkrh usyp rjyo"

    receiver = "abdulganiyu9023@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver, message)

