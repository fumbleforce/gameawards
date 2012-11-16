from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.utils import timezone
from runs.forms import GameRegistrationForm
from runs.models import Game, Run




def game_registration_request(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/members/login/')
    if request.method == 'POST':
        form = GameRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            game = Game()
            game.name=form.cleaned_data['name']
            game.description = form.cleaned_data['description']
            game.added_date = timezone.now()
            game.icon = form.cleaned_data['icon']
            game.team = form.cleaned_data['team']
            dev = Developer(user=request.user, role='Project leader', game=game)
            dev.save()
            game.leader = dev
            run = Run.Objects.get(current_run = True)
            game.save()
            return HttpResponseRedirect('/members/profile/')
        else:
            context = {'form':form}
    else:
        form = GameRegistrationForm()
        context = {'form':form}
    return render_to_response(
        'runs/register_game.html', 
        context, 
        context_instance=RequestContext(request))




def game_list_request(request):
    curr_run = Run.objects.get(current_run = True)
    game_list = Game.objects.filter(run=curr_run)
    context = {'games':game_list}
    return render_to_response(
        'runs/game_list.html', 
        context, 
        context_instance=RequestContext(request))


def game_request(request, game_id):
    game = Game.objects.get(pk=game_id)
    context = {'game':game}
    return render_to_response(
        'runs/game.html', 
        context, 
        context_instance=RequestContext(request))
















