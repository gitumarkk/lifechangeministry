# Create your views here.
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages


# Project
from frontpages.forms import ContactForm
from lcm.utils import contact_email


def home(request):
    context = {}
    return render(request,
                  "frontpages/home.html",
                  context)


def about(request):
    context = {}
    return render(request,
                  "frontpages/about.html",
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
