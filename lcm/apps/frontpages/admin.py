# Project
from django.contrib import admin

# Project
from lcm.apps.backend.forms import EventForm, StoryForm
from lcm.apps.backend.models import Event, Story


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',
                    'event_date',
                    'created_at')
    form = EventForm

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',
                    'created_at')
    form = StoryForm

admin.site.register(Event, EventAdmin)
admin.site.register(Story, StoryAdmin)
