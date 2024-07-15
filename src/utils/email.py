from email.mime.image import MIMEImage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .output import output_ERROR, output_INFO
from .config import util_settings


EMAIL_HOST = util_settings.EMAIL_HOST
EMAIL_PORT = util_settings.EMAIL_PORT
EMAIL_FROM = util_settings.EMAIL_FROM
EMAIL_PASSWORD = util_settings.EMAIL_PASSWORD
EMAIL_BCC = util_settings.EMAIL_BCC


def init_data():
    email_info = MIMEMultipart("related")
    email_info["From"] = EMAIL_FROM
    email_info["Bcc"] = EMAIL_BCC
    return email_info


def get_image():
    with open("public/siemav.png", "rb") as image_file:
        image_data = image_file.read()
        image = MIMEImage(image_data)
        image.add_header("Content-ID", "<image1>")
        image.add_header(
            "Content-Disposition", "inline", filename="siemav.png"
        )
        return image


def send_mail_msg(email_info):
    try:
        print(EMAIL_HOST)
        print(EMAIL_PORT)
        print(EMAIL_FROM)
        print(EMAIL_PASSWORD)
        print(EMAIL_BCC)
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as servidor_smtp:
            servidor_smtp.starttls()
            servidor_smtp.login(EMAIL_FROM, EMAIL_PASSWORD)
            servidor_smtp.send_message(email_info)
            output_INFO(f"Enviando correo... {email_info['To']}")
            servidor_smtp.quit()
        return True
    except Exception as e:
        output_ERROR(f"send_mail_msg -> {e}")
        raise e


def send_verification_code(to, content):
    try:
        email_info = init_data()
        
        email_info["To"] = to
        email_info["Subject"] = "Codigo de verificacion"
        with open(
            "utils/mail/verification-code.html", "r", encoding="utf-8"
        ) as html_file:
            html = html_file.read()
            html = html.replace("{content}", content)
        part2 = MIMEText(html, "html")
        email_info.attach(part2)
        email_info.attach(get_image())
        return send_mail_msg(email_info)
    except Exception as e:
        output_ERROR(f"send_verification_code -> {e}")
        raise e


def send_user_credentials(to, content):
    try:
        email_info = init_data()
        email_info["To"] = to
        email_info["Subject"] = "Credenciales de acceso"
        with open(
            "utils/templates/user-credential.html", "r", encoding="utf-8"
        ) as html_file:
            html = html_file.read()
            html = html.replace("{username}", content["username"])
            html = html.replace("{password}", content["password"])
            # html = html.replace("{origin}", content["origin"])
        part2 = MIMEText(html, "html")
        email_info.attach(part2)
        email_info.attach(get_image())
        return send_mail_msg(email_info)
    except Exception as e:
        output_ERROR(f"send_user_credentials -> {e}")
        raise e
