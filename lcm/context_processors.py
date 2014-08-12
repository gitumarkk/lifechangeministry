# Django
from django.core.urlresolvers import reverse


def highlight_active_menu(request):
    if reverse("about") in request.path:
        return {'about_is_active': True}

    # elif reverse("stories") in request.path:
    #     return {'stories': True}

    # elif reverse("partners") in request.path:
    #     return {'partners': True}

    elif reverse("ministry") in request.path:
        return {'ministry_is_active': True}

    elif reverse("contact") in request.path:
        return {'contact_is_active': True}

    elif "events" in request.path:
        return {"events_nav_is_active": True}

    elif "blog" in request.path:
        return {"blog_is_active": True}
    else:
        # This is because the home path is '\'
        return {"home_is_active": True}


