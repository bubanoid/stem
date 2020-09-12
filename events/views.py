from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import Event, EventImage, EventTag, EventPartner

class EventView(View):
    def get(self, request):
        new_event_list = Event.objects.filter(conducted=False)
        old_event_list = Event.objects.filter(conducted=True)

        context = {
            'new_event_list':new_event_list,
            'old_event_list':old_event_list
        }
        return render(request, 'events/event_list.html', context)

class EventDatailView(View):
    def get(self, request, slug):
        event = get_object_or_404(Event, slug = slug)
        return render (request, 'events/event.html', {'event':event})

        
