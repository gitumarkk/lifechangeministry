# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages


# Project
from lcm.apps.backend.models import Event, Story, Partner
from lcm.apps.frontpages.forms import ContactForm
from lcm.utils import contact_email


def home(request):
    latest_story = Story.get_latest_story()
    latest_event = Event.get_latest_event()

    context = {"latest_story": latest_story,
               "latest_event": latest_event}
    return render(request,
                  "frontpages/home.html",
                  context)


def about(request):
    context = {}
    return render(request,
                  "frontpages/about.html",
                  context)


def stories(request):
    current_story = Story.get_latest_story()
    stories = Story.get_stories()

    context = {"current_story": current_story,
                "stories": stories}
    return render(request,
                  "frontpages/stories.html",
                  context)

def story(request, _id):
    current_story = get_object_or_404(Story, pk=_id)
    stories = Story.get_stories()

    context = {"current_story": current_story,
                "stories": stories}
    return render(request,
                  "frontpages/stories.html",
                  context)

def partners(request):
    partners = Partner.get_partners()
    context = {"partners": partners}
    return render(request,
                  "frontpages/partners.html",
                  context)

def partner(request, _id):
    partner = get_object_or_404(Partner, pk=_id)
    context = {"partner": partner}
    return render(request,
                 "frontpages/partner.html",
                  context)


def ministry(request):
    context = {}
    return render(request,
                  "frontpages/ministry.html",
                  context)


def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            contact_email(contact.name, contact.email, contact.message)
            # Assumes if no error the e-mail has been sent
            contact.sent = True
            contact.save()
            messages.success(request,
                             "Thank you we have received your message.")
            return redirect(reverse("home"))
        else:
            messages.error(request, "There were errors on the form.", extra_tags="danger")
    else:
        contact_form = ContactForm()
    context = {"contact_form": contact_form}
    return render(request,
                  "frontpages/contact.html",
                  context)