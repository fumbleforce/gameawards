from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from content.models import General

def info_request(request):
    rules = General.objects.get(title='rules')
    categories = General.objects.get(title='categories')
    general = General.objects.get(title='general')
    
    return render_to_response(
        'content/info.html', 
        {
        'rules': rules,
        'categories': categories,
        'general': general,
        },
        context_instance=RequestContext(request))
