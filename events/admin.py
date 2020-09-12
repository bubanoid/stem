from django.contrib import admin
from .models import Event, EventImage, EventTag, EventPartner

admin.site.register(Event)
admin.site.register(EventImage)
admin.site.register(EventTag)
admin.site.register(EventPartner)