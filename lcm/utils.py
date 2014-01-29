# Django
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

# FROM THIRD PARTY
import mandrill

def contact_email(name, email, message, id=False):
        context_email = {"message": message, "email": email, "name": name}

        html = get_template("email/contact.html").render(Context(context_email))
        text = get_template("email/contact.txt").render(Context(context_email))

        mandrill_email = mandrill.Mandrill(settings.MANDRILL_KEY)

        mandrill_data = {
                "html": html,
                "text": text,
                "from_email": email,
                "from_name": name,
                "to": [{"email": settings.TO_EMAIL}]
            }

        return mandrill_email.messages.send(message=mandrill_data)
