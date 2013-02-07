from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from django.utils import timezone
from gallery.forms import GamePicForm
from runs.models import Game
from gallery.models import GamePic

def add_gamepic_request(request,game_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    
    g = Game.objects.get(pk = game_id)
    images = GamePic.objects.filter(game=g)
    if request.method == 'POST':
        form = GamePicForm(request.POST, request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            p.added_date = timezone.now()
            p.image = request.FILES['image']
            p.game = get_object_or_404(Game, pk=game_id)
            p.owner = request.user        
            p.save()    
            if p.game_icon:
                gs = GamePic.objects.filter(game=g, game_icon=True)
                for gp in gs:
                    if gp.id != p.id:
                        gp.game_icon=False;
                        gp.save()
            

            return HttpResponseRedirect('/gallery/add_game_pic/'+str(game_id))
        else:
            context = {'form':form, 'images':images}
    else:
        form = GamePicForm()
        
        context = {'form':form,'images':images}
    return render_to_response(
        'gallery/add_game_pic.html', 
        context, 
        context_instance=RequestContext(request))
