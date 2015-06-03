# django
from django.utils.translation import ugettext_lazy as _
from django import forms

# Project
from lcm.apps.frontpages.models import Contact

# Third party
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                           'class': 'required form-control'},
                                                            ),
                                label=_("Name"))

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address',
                                                            'class': 'required form-control',
                                                            "maxlength": 75},
                                                               ),
                             label=_("Email address"))

    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message',
                                                            'class': 'required form-control'},
                                                               ),
                             label=_("Message"))

    captcha = CaptchaField()

    class Meta:
        model = Contact
        exclude = ["created_at"]
        fields = ["name", "email", "message"]
