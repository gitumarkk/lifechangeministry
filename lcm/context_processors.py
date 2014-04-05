# Django
from django.core.urlresolvers import reverse


def highlight_active_menu(request):
    if reverse("about") in request.path:
        return {'about': True}

    elif reverse("stories") in request.path:
        return {'stories': True}

    elif reverse("partners") in request.path:
        return {'partners': True}

    elif reverse("ministry") in request.path:
        return {'ministry': True}

    elif reverse("contact") in request.path:
        return {'contact': True}

    elif "events" in request.path:
        return {"events_nav": True}

    elif reverse("home") in request.path:
        return {"home": True}
