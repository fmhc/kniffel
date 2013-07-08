# Create your views here.
from django.template import RequestContext, Context, loader
from kniffelApp.models import *
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.sessions.backends.db import SessionStore


def kniffel(request):
    
    latest_game_list = game.objects.all().order_by('start')[:3]
    latest_player_list = player.objects.all().order_by('id')[:3]
    
    
    t = loader.get_template('kniffel/kniffel.html')
    c = Context({
        'latest_game_list': latest_game_list,
        'latest_player_list': latest_player_list,
    })
    return HttpResponse(t.render(c))

def kniffel_start(request):
    s = SessionStore()
    s['chaos'] = "auf jeden Fall"
    request.session['start'] = True
    request.session['ccx'] = "Haha es funzt"
    
    t = loader.get_template('kniffel/kniffel.html')
    c = Context({
        'chaos': request.session['ccx'],
    })
    
    c.update(csrf(request))
    return HttpResponse(t.render(c))
    s.save()
    #c = {}
    
    # ... view code here
    #return render_to_response("kniffel/kniffel.html", c)    
    #latest_game_list = game.objects.all().order_by('start')[:3]
    #latest_player_list = player.objects.all().order_by('id')[:3]
    
    #game_name = "Neues Spiel"
    
    #t = loader.get_template('kniffel/kniffel.html')
    #c = RequestContext(request, {
    #    'gamename': game_name,
    # })
    # return HttpResponse(t.render(c))

def kniffel_w_hold(request, w_id):
    
    #latest_game_list = game.objects.all().order_by('start')[:3]
    #latest_player_list = player.objects.all().order_by('id')[:3]
    
    hold_w_id = w_id
    
    t = loader.get_template('kniffel/kniffel.html')
    c = Context({
        'hold_w_id': hold_w_id,
    })
    return HttpResponse(t.render(c))

def highscore(request):
    latest_game_list = game.objects.all().order_by('start')[:3]
    latest_player_list = player.objects.all().order_by('id')[:3]
    t = loader.get_template('kniffel/highscore.html')
    c = Context({
        'latest_game_list': latest_game_list,
        'latest_player_list': latest_player_list,
    })
    return HttpResponse(t.render(c))


def jsjquery(request):
    t = loader.get_template('js/jquery-1.10.2.js')
    c = Context({
        'test': None,
    })
    return HttpResponse(t.render(c))


def bootstrapcss(request):
    t = loader.get_template('css/bootstrap.css')
    c = Context({
        'test': None,
    })
    return HttpResponse(t.render(c))

def bootstrapresponsivecss(request):
    t = loader.get_template('css/bootstrap-responsive.css')
    c = Context({ })
    return HttpResponse(t.render(c))

def home(request):
    latest_game_list = game.objects.all().order_by('start')[:3]
    latest_player_list = player.objects.all().order_by('id')[:3]
    t = loader.get_template('index.html')
    c = Context({
        'latest_game_list': latest_game_list,
        'latest_player_list': latest_player_list,
    })
    return HttpResponse(t.render(c))

def download(request):
    t = loader.get_template('kniffel/download.html')
    c = Context({ })
    return HttpResponse(t.render(c))

def impressum(request):
    t = loader.get_template('kniffel/impressum.html')
    c = Context({ })
    return HttpResponse(t.render(c))
