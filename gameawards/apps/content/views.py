from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from content.models import General

def info_request(request):
    rules = General.objects.get(title='rules')
    categories = General.objects.get(title='categories')
    organizers = General.objects.get(title='organizers')
    faq = General.objects.get(title='faq')
    guides = General.objects.get(title='guides')
    
    return render_to_response(
        'content/info.html', 
        {
        'rules': rules,
        'categories': categories,
        'organizers': organizers,
        'faq':faq,
        'guides':guides,
        },
        context_instance=RequestContext(request))
