# Create your views here.
from django.template import Context, loader
from kniffelApp.models import *
from django.http import HttpResponse

def kniffel(request):
    
    latest_game_list = game.objects.all().order_by('start')[:3]
    latest_player_list = player.objects.all().order_by('id')[:3]
    t = loader.get_template('kniffel/kniffel.html')
    c = Context({
        'latest_game_list': latest_game_list,
        'latest_player_list': latest_player_list,
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
