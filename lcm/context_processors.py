# Django
from django.core.urlresolvers import reverse


def highlight_active_menu(request):
    if reverse("about") == request.path:
        return {'about': True}
    elif reverse("contact") == request.path:
        return {'contact': True}
    elif reverse("home") == request.path:
        return {"home": True}
