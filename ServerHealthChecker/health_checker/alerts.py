import smtplib
from email.message import EmailMessage


def send_alert(failed_services):

    if not failed_services:
        return

    msg = EmailMessage()
    msg["Subject"] = "Server Health Alert"
    msg["From"] = "adiauwase060@gmail.com"
    msg["To"] = "uwaseadia7@gmail.com"

    msg.set_content("\n".join(failed_services))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(
                "adiauwase060@gmail.com",
                "nnyo jfix gjcg hfqg"
            )

            smtp.send_message(msg)

        print("Alert email sent successfully")

    except Exception as e:
        print("Email failed:", e)