from django.shortcuts import render_to_response, get_object_or_404
from news.models import Newspost

def index(request):
    newspost_list = Newspost.objects.all().order_by('-pub_date')[:5]
    return render_to_response('news/index.html', {'newspost_list': newspost_list})


def detail(request, newspost_id):
    p = get_object_or_404(Newspost, pk=newspost_id)
    return render_to_response('news/detail.html', {'post': p})
