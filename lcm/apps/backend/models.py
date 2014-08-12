# Python
from datetime import datetime
import os, time

# Django
from django.template.defaultfilters import date
from django.db import models
from django.db.models import Q

# Third Party
from imagekit.processors import ResizeToFit
from imagekit.models import ImageSpecField
from sorl.thumbnail import ImageField


class Event(models.Model):
    def generate_new_filename(instance, filename):
        ext = os.path.splitext(filename)[1] # get file extension
        image_name = "%s%s" % (int(time.time() * 100000), ext)
        return "%s%s%s" % ("event", os.sep, image_name)

    title = models.CharField(max_length=50)
    image = ImageField(upload_to=generate_new_filename)
    thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFit(100, 100, upscale=True)],
                                    format='JPEG',
                                    options={'quality': 60})
    description = models.TextField(null=True, blank=True)
    recurring = models.BooleanField(default=False)
    event_date = models.DateTimeField('Event Date')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_event_date(self):
        if self.recurring:
            return "%s happens every %s" % (self.title, date(self.event_date, "l"))
        else:
            return "%s is happening on %s" % (self.title, date(self.event_date, "j F o"))

    @classmethod
    def get_latest_event(cls):
        return cls.objects.filter(Q(event_date__gte=datetime.now()) |
                                  Q(recurring=True)).order_by("event_date").first()

    @classmethod
    def get_events(cls):
        return cls.objects.filter(Q(event_date__gte=datetime.now()) |
                                  Q(recurring=True)).order_by("event_date").all()


class Story(models.Model):
    def generate_new_filename(instance, filename):
        ext = os.path.splitext(filename)[1] # get file extension
        image_name = "%s%s" % (int(time.time() * 100000), ext)
        return "%s%s%s" % ("event", os.sep, image_name)

    title = models.CharField(max_length=50)
    image = ImageField(upload_to=generate_new_filename, null=True, blank=True)
    thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFit(100, 100, upscale=True)],
                                    format='JPEG',
                                    options={'quality': 60})
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    @classmethod
    def get_latest_story(cls):
        return cls.objects.order_by("-created_at").first()


    @classmethod
    def get_stories(cls):
        return cls.objects.order_by("-created_at").all()


class Partner(models.Model):
    def generate_new_filename(instance, filename):
        ext = os.path.splitext(filename)[1] # get file extension
        image_name = "%s%s" % (int(time.time() * 100000), ext)
        return "%s%s%s" % ("partners", os.sep, image_name)

    title = models.CharField(max_length=50)
    image = ImageField(upload_to=generate_new_filename, null=True, blank=True)
    thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFit(100, 100, upscale=True)],
                                    format='JPEG',
                                    options={'quality': 60})
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    @classmethod
    def get_partners(cls):
        return cls.objects.order_by("-created_at").all()
