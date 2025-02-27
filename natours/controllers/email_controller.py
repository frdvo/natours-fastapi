from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from natours.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_TLS=settings.MAIL_TLS,
    MAIL_SSL=settings.MAIL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS,
    VALIDATE_CERTS=settings.VALIDATE_CERTS,
)


email_client = FastMail(conf)


def render_email_message(reset_url):

    html = f"""
    <p> reset your password visiting this url: {reset_url} </p> 
    """

    return html


async def send_password_reset_email(email, html):
    message = MessageSchema(
        subject="reset password token for natours app (expire in 15 minutes)",
        recipients=[email],
        body=html,
        subtype="html",
    )
    email_client = FastMail(conf)
    await email_client.send_message(message)


async def send_password_reset_confirmation(email):
    message = MessageSchema(
        subject="you changed your password",
        recipients=[email],
        body=f"<p> password for email: {email} was successfully changed </p> ",
        subtype="html",
    )
    client = FastMail(conf)
    await client.send_message(message)
