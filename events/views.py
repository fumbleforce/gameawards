from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from events.models import Event
from django.utils import timezone

def event_list(request):
    events = Event.objects.filter(date_opens__lte=timezone.now(), date_closes__gte=timezone.now)
    return render_to_response(
        'events/event_list.html', 
        {'events':events}, 
        context_instance=RequestContext(request))
    
    

def register_to_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    embed = event.embed()
    return render_to_response(
        'events/register_to_event.html',
        {'event':event, 'embed':embed},
        context_instance=RequestContext(request))
        
