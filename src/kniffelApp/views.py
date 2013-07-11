# Create your views here.
from django.template import RequestContext, Context, loader
from kniffelApp.models import *
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.sessions.backends.db import SessionStore
from django import forms
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache

@csrf_protect
@never_cache
def kniffel(request):
    latest_game_list = game.objects.all().order_by('start')[:3]
    latest_player_list = player.objects.all().order_by('id')[:3]
    if request.method == 'POST':
        print "request post"
        
    request.session['start'] = True
    request.session['ccx'] = "Haha es funzt"

    
    return render_to_response("kniffel/kniffel.html",
                          {'playername': request.user,
                           'sess': request,
                           'latest_game_list': latest_game_list,
                           'latest_player_list': latest_player_list,
                           },
                            context_instance=RequestContext(request))
@csrf_protect
def kniffel_next(request):
    if "game_round" in request.session:
        ro = request.session['game_round']
        #ro = game_round()
    else:
        ro = game_round()    
    
    ro.wurf = 0    
        
    ro.game = request.session['game']
    
    
    # Wird noch Probleme verursachen, muss wo anders eingebaut werden mit User-Verknuepfung - sonst funktioniert Multiplayer nicht!
    #
    #   runde = 0
    #   runde = int(runde) + 1
   
    ro.game.nextround()
    request.session['game_round'] = ro
    ro.w1.hold = False
    ro.w2.hold = False
    ro.w3.hold = False
    ro.w4.hold = False
    ro.w5.hold = False    
    #wuerfeln
    diceset = ro.roll()
    request.session['game_round'] = ro
    # = diceset[1]
    request.session['diceset'] = diceset
    
    #if "game" in request.session:
    #    request.session['game'] = None
    #    del request.session['game']
    
    #if "instanz" in request.session:    
    #    request.session['instanz'] = None
    #    del request.session['instanz']
    
    
    return render_to_response("kniffel/kniffel.html",
                          {'playername': request.user,
                           'gamename': None,
                           'sess': request,
                           'diceset': request.session['diceset'],
                           'wurf': request.session['game_round'].wurf,
                           },
                          context_instance=RequestContext(request))


@csrf_protect
def kniffel_roll(request):
    if "game_round" in request.session:
        ro = request.session['game_round']
        #ro = game_round()
    else:
        ro = game_round()
        #request.session['game_round'] = ro
        
    ro.game = request.session['game']
    request.session['game_round'] = ro
    
    # Wird noch Probleme verursachen, muss wo anders eingebaut werden mit User-Verknuepfung - sonst funktioniert Multiplayer nicht!
    #
    #   runde = 0
    #   runde = int(runde) + 1
   
    #ro.game.nextround()
    #wuerfeln
    diceset = ro.roll()
    # = diceset[1]
    request.session['diceset'] = diceset
    
    #if "game" in request.session:
    #    request.session['game'] = None
    #    del request.session['game']
    
    #if "instanz" in request.session:    
    #    request.session['instanz'] = None
    #    del request.session['instanz']
    
    
    return render_to_response("kniffel/kniffel.html",
                          {'playername': request.user,
                           'gamename': None,
                           'sess': request,
                           'diceset': request.session['diceset'],
                           'wurf': request.session['game_round'].wurf,
                           },
                          context_instance=RequestContext(request))


    
@csrf_protect
def kniffel_stop(request):
    if request.method == 'POST':
        print "request post - kniffel_stop"

    request.session['start'] = False
    if "game_round" in request.session:
        request.session['game_round'] = None
        del request.session['game_round']
    
    if "game" in request.session:
        request.session['game'] = None
        del request.session['game']
    
    if "instanz" in request.session:    
        request.session['instanz'] = None
        del request.session['instanz']
    
    if "diceset" in request.session:    
        request.session['diceset'] = None
        del request.session['diceset']
    
    if "playerlist" in request.session:    
        request.session['playerlist'] = None
        del request.session['playerlist']
    
    return render_to_response("kniffel/kniffel.html",
                          {'playername': request.user,
                           'gamename': None,
                           'sess': request
                           },
                          context_instance=RequestContext(request))
    
    
@csrf_protect
def kniffel_start(request):
    if request.method == 'POST':
        print "request post"

        request.session['start'] = True
        
        if not instanz in request.session:
            request.session['instanz'] = instanz()
    
        if "gamename" in request.POST:
            if request.POST['gamename'] != "":
                gamename = request.POST['gamename']
            else:
                gamename = "Spiel"
            
        if "player1" in request.POST:
            player1 = request.POST['player1']
        else:
            if request.user.is_authenticated():
                player1 = str(request.user)
            else:
                player1 = "Spieler"
        
        if "player2" in request.POST:
            player2 = request.POST['player2']
        else:
            player2 = None
        
        if "player3" in request.POST:
            player3 = request.POST['player3']
        else:
            player3 = None
        
        if "player4" in request.POST:
            player4 = request.POST['player4']
        else:
            player4 = None    

        newgame = request.session['instanz'].new_game(str(gamename), str(player1), str(player2), str(player3), str(player4))
       
        request.session['playerlist'] = []
        for plyr in newgame.player.all():
            
            x = result()
            x.game = newgame 
            x.player = plyr
            x.save()
            
            request.session['playerlist'].append(x)
            
        #newgame.
        
        newgame.save()
        request.session['game'] = newgame
        
        
        return kniffel_next(request)
    #tempgame = request.session['']    
#     return render_to_response("kniffel/kniffel.html",
#                           {'playername': request.user,
#                            'gamename': request.session['game'].name,
#                            'sess': request
#                            },
#                           context_instance=RequestContext(request))
   
    #game_name = "Neues Spiel"
    
    #t = loader.get_template('kniffel/kniffel.html')
    #c = RequestContext(request, {
    #    'gamename': game_name,
    # })
    # return HttpResponse(t.render(c))

@csrf_protect
def kniffel_w_hold(request, w_id):
    
    #latest_game_list = game.objects.all().order_by('start')[:3]
    #latest_player_list = player.objects.all().order_by('id')[:3]
    #gr = request.session['game_round']
    
    hold_w_id = w_id
    
    if int(w_id) == 1:
        if request.session['game_round'].w1.hold == False:
            request.session['game_round'].w1.hold = True
        else:
            request.session['game_round'].w1.hold = False

    if int(w_id) == 2:
        if request.session['game_round'].w2.hold == False:
            request.session['game_round'].w2.hold = True
        else:
            request.session['game_round'].w2.hold = False

    if int(w_id) == 3:
        if request.session['game_round'].w3.hold == False:
            request.session['game_round'].w3.hold = True
        else:
            request.session['game_round'].w3.hold = False

    if int(w_id) == 4:
        if request.session['game_round'].w4.hold == False:
            request.session['game_round'].w4.hold = True
        else:
            request.session['game_round'].w4.hold = False

    if int(w_id) == 5:
        if request.session['game_round'].w5.hold == False:
            request.session['game_round'].w5.hold = True
        else:
            request.session['game_round'].w5.hold = False

    
    return render_to_response("kniffel/kniffel.html",
                          {'playername': request.user,
                           'gamename': request.session['game'].name,
                           'diceset': request.session['game_round'].refresh_state(),
                           'sess': request,
                           'hold_w_id': hold_w_id,
                           },
                            context_instance=RequestContext(request))  

@csrf_protect
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

@csrf_protect
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
