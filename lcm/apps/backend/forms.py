# Django
from django import forms
from lcm.apps.backend.models import Event, Story

# Project

# Third Party
from tinymce.widgets import TinyMCE

class EventForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Event


class StoryForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Story
