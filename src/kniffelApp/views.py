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

    if not "diceset" in request.session:
        request.session['diceset'] = None
        
    return render_to_response("kniffel/kniffel.html",
                          {'playername': request.user,
                           'sess': request,
                           'diceset': request.session['diceset'],
                           'latest_game_list': latest_game_list,
                           'latest_player_list': latest_player_list,
                           },
                            context_instance=RequestContext(request))
@csrf_protect
def kniffel_next(request, args=None):
    next_process_running = True
    errormsg = None

    print "-- views - kniffel_next"
    msg = "Testmessage fuer msg"
    if "game_round" in request.session:
        print "game round exists"
        ro = request.session['game_round']
        
        #ro = game_round()
    else:
        print "game round does not exist"
        ro = game_round()    
    print "game round:"
    print ro
#    print msg
    
    einfach = {}
    i = 0
    for entr in request.session['playerlist']:
        einfach[i] = entr
        
    
    print einfach
    print einfach.keys()
    for ei in einfach.values():
        print ei
    #print einfach[1]
    
    
    if request.GET:
        msg = "existiert: request.GET\n"
        msg = msg + str(request.GET) + "\n"
        if request.GET['choose']:
            msg = msg + "Es wurde folgende Wahl getroffen (request.GET['choose']): "
            msg = msg + str(request.GET['choose']) + "\n"
            cho = request.GET['choose']
            
            # Playerlist
            new_res = request.session['playerlist']            
            msg = msg + "\n\n Playerlist (request.session['playerlist']): \n" + str(new_res) + "\n"
                      
            pot_res = check_diceset(request.session['diceset'])
            
            msg = msg + "\n\n potentielles Ergebnis (check_diceset(request.session['diceset']):\n"
            
            #msg = msg + str(pot_res.r1er)
            
            
            player_number = 0
            
            if str(cho) == "r1er":
                msg = msg + "es wurden r1er gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].r1er == None:
                    msg = msg + str(new_res[player_number].r1er) + "\n"
                    new_res[player_number].r1er = pot_res.r1er
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass
            if cho == "r2er":
                msg = msg + "es wurden r2er gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].r2er == None:
                    msg = msg + str(new_res[player_number].r2er) + "\n"
                    new_res[player_number].r2er = pot_res.r2er
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass           
            if cho == "r3er":
                msg = msg + "es wurden r3er gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].r3er == None:
                    msg = msg + str(new_res[player_number].r3er) + "\n"
                    new_res[player_number].r3er = pot_res.r3er
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass                   
            if cho == "r4er":
                msg = msg + "es wurden r4er gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].r4er == None:
                    msg = msg + str(new_res[player_number].r4er) + "\n"
                    new_res[player_number].r4er = pot_res.r4er
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass              
            if cho == "r5er":
                msg = msg + "es wurden r5er gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].r5er == None:
                    msg = msg + str(new_res[player_number].r5er) + "\n"
                    new_res[player_number].r5er = pot_res.r5er
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass    
            if cho == "r6er":
                msg = msg + "es wurden r6er gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].r6er == None:
                    msg = msg + str(new_res[player_number].r6er) + "\n"
                    new_res[player_number].r6er = pot_res.r6er
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass      
            
            if cho == "rfullhouse":
                msg = msg + "es wurden rfullhouse gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].rfullhouse == None:
                    msg = msg + str(new_res[player_number].rfullhouse) + "\n"
                    new_res[player_number].rfullhouse = pot_res.rfullhouse
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass  
            
            if cho == "r3p":
                msg = msg + "es wurden r3p gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].r3p == None:
                    msg = msg + str(new_res[player_number].r3p) + "\n"
                    new_res[player_number].r3p = pot_res.r3p
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass  
            
            if cho == "r4p":
                msg = msg + "es wurden r4p gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].r4p == None:
                    msg = msg + str(new_res[player_number].r4p) + "\n"
                    new_res[player_number].r4p = pot_res.r4p
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass                                         
            
            if cho == "rchance":
                msg = msg + "es wurden Chance gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].rchance == None:
                    msg = msg + str(new_res[player_number].rchance) + "\n"
                    new_res[player_number].rchance = pot_res.rchance
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass      
           
            if cho == "rgrossestr":
                msg = msg + "es wurden Grosse Strasse gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].rgrossestr == None:
                    msg = msg + str(new_res[player_number].rgrossestr) + "\n"
                    new_res[player_number].rgrossestr = pot_res.rgrossestr
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass    

            if cho == "rkleinestr":
                msg = msg + "es wurden Grosse Strasse gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].rkleinestr == None:
                    msg = msg + str(new_res[player_number].rkleinestr) + "\n"
                    new_res[player_number].rkleinestr = pot_res.rkleinestr
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass    
             
            if cho == "rkniffel":
                msg = msg + "es wurden Kniffel gewaehlt\n"
                #msg = msg + "Es wurde folgende Wahl getroffen:\nr1er\n"
#                msg = msg + str(new_res.r1er) + "\n"
#                msg = msg + str(new_res.r1er) + "\n"
                if new_res[player_number].rkniffel == None:
                    msg = msg + str(new_res[player_number].rkniffel) + "\n"
                    new_res[player_number].rkniffel = pot_res.rkniffel
                else:
                    msg = msg + "\n--- schon belegt \n"
                    next_process_running = False
                    errormsg = "Wurde schon gewaehlt, bitte eine andere Option waehlen!"
                pass      
            
            bonus_sum = 0
            if not new_res[player_number].r1er == None:
                bonus_sum = bonus_sum + int(new_res[player_number].r1er)
            if not new_res[player_number].r2er == None:
                bonus_sum = bonus_sum + int(new_res[player_number].r2er)
            if not new_res[player_number].r3er == None:
                bonus_sum = bonus_sum + int(new_res[player_number].r3er)
            if not new_res[player_number].r4er == None:
                bonus_sum = bonus_sum + int(new_res[player_number].r4er)
            if not new_res[player_number].r5er == None:
                bonus_sum = bonus_sum + int(new_res[player_number].r5er)
            if not new_res[player_number].r6er == None:
                bonus_sum = bonus_sum + int(new_res[player_number].r6er)                                                
            
            if bonus_sum > 63:
                new_res[player_number].rbonus = 35
            else:
                new_res[player_number].rbonus = 0
            
            #request.GET['choose'] = None
        
    #if request.POST:
    #    print request.POST
    if next_process_running == True:   
        
        
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
    
        arr = []
        xi = 0
        res_pl = request.session['playerlist']
        for item in res_pl:
            arr.insert(xi, item)
            xi  = xi + 1
    
            
        #game_id = ro.game.pk
        #player_id = 1
        #act_res = result.objects.get(game__id=game_id)
        act_res = arr[0]
        #act_res = result.objects.get(player__id=player_id, game__id=game_id)
    
        # WUERFELN
        diceset = ro.roll()
        msg = msg + u"--- es wurde gewuerfelt ---\n"
        request.session['game_round'] = ro
        request.session['diceset'] = diceset
        request.session['act_res'] = act_res
        request.session['pot_res'] = check_diceset(diceset)

    # DICESET
    msg = msg + "\n\nDiceset (request.session['diceset']):\n"
    msg = msg + str(request.session['diceset'])
    
    #if "game" in request.session:
    #    request.session['game'] = None
    #    del request.session['game']
    
    #if "instanz" in request.session:    
    #    request.session['instanz'] = None
    #    del request.session['instanz']
    request.session['msg'] = msg
    request.session['error'] = errormsg
    
    return render_to_response("kniffel/kniffel.html",
                          {'playername': request.user,
                           'gamename': None,
                           'sess': request,
                           'message': msg,
                           'error'  : errormsg,
                           'pot_res': request.session['pot_res'],
                           'diceset': request.session['diceset'],
                           'wurf': request.session['game_round'].wurf,
                           },
                          context_instance=RequestContext(request))

def check_diceset(diceset, bonusdiceset=False):
    pot_res = result()
    pot_res.r1er = c1er(diceset) 
    pot_res.r2er = c2er(diceset) 
    pot_res.r3er = c3er(diceset) 
    pot_res.r4er = c4er(diceset) 
    pot_res.r5er = c5er(diceset) 
    pot_res.r6er = c6er(diceset) 
    if bonusdiceset:
        pot_res.rbonus = cbonus(bonusdiceset)
    pot_res.r3p = c3p(diceset) 
    pot_res.r4p = c4p(diceset) 
    pot_res.rfullhouse = cfullhouse(diceset) 
    pot_res.rkleinestr = ckleinestr(diceset) 
    pot_res.rgrossestr = cgrossestr(diceset)
    pot_res.rkniffel = ckniffel(diceset)
    pot_res.rchance = cchance(diceset)
    
    pot_res.xsum1 = pot_res.sum_oben()
    return pot_res
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
    request.session['error'] = None
    
    # Wird noch Probleme verursachen, muss wo anders eingebaut werden mit User-Verknuepfung - sonst funktioniert Multiplayer nicht!
    #
    #   runde = 0
    #   runde = int(runde) + 1
   
    #ro.game.nextround()
    #wuerfeln
    diceset = ro.roll()
    # = diceset[1]
    request.session['diceset'] = diceset
    print diceset
    #print ro.game.build_check(diceset)
    # UPDATE Possible RESULTSET 
    
    pot_res = result()
    pot_res.r1er = c1er(diceset) 
    pot_res.r2er = c2er(diceset) 
    pot_res.r3er = c3er(diceset) 
    pot_res.r4er = c4er(diceset) 
    pot_res.r5er = c5er(diceset) 
    pot_res.r6er = c6er(diceset) 
    pot_res.sum1 = pot_res.sum_oben()
    pot_res.rbonus = 0 #cbonus(pot_res)
    pot_res.r3p = c3p(diceset) 
    pot_res.r4p = c4p(diceset) 
    pot_res.rfullhouse = cfullhouse(diceset) 
    pot_res.rkleinestr = ckleinestr(diceset) 
    pot_res.rgrossestr = cgrossestr(diceset)
    pot_res.rkniffel = ckniffel(diceset)
    pot_res.rchance = cchance(diceset)
    request.session['pot_res'] = pot_res
    #request.session['pot_res'] = check_diceset(diceset)
    #request.session['resultset'] = ro.game.build_check(diceset)
    #if "game" in request.session:
    #    request.session['game'] = None
    #    del request.session['game']
    
    #if "instanz" in request.session:    
    #    request.session['instanz'] = None
    #    del request.session['instanz']
    
    
    return render_to_response("kniffel/kniffel.html",
                          {'playername': request.user,
                           'sess': request,
                           'pot_res': pot_res,
                           'diceset': request.session['diceset'],
                           'wurf': request.session['game_round'].wurf,
                           },
                          context_instance=RequestContext(request))


    
@csrf_protect
def kniffel_stop(request):
    print "--- GAME WIRD GESTOPPT ---"
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
    
    
    request.session['msg'] = None
    return render_to_response("kniffel/kniffel.html",
                          {'playername': request.user,
                           'sess': request,
                           'pot_res': None,
                           'diceset': None,
                           'wurf': None,
                           'message': "",
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
                gamename = "Kniffelrunde"
        else:
            gamename = "Kniffelrunde"
            
        if "player1" in request.POST:
            if request.POST['player1'] != "":
                player1 = request.POST['player1']
            else:
                if request.user.is_authenticated():
                    player1 = str(request.user)
                else:
                    player1 = "Spieler"
        else:
            if request.user.is_authenticated():
                player1 = str(request.user)
            else:
                player1 = "Spieler"
        
        if "player2" in request.POST:
            if request.POST['player2'] != "":
                player2 = request.POST['player2']
            else:
                player2 = None
        else:
            player2 = None
        
        if "player3" in request.POST:
            if request.POST['player3'] != "":
                player3 = request.POST['player3']
            else:
                player3 = None
        else:
            player3 = None
        
        if "player4" in request.POST:
            if request.POST['player4'] != "":
                player4 = request.POST['player4']
            else:
                player4 = None
        else:
            player4 = None    

        newgame = request.session['instanz'].new_game(str(gamename), player1, player2, player3, player4)
       
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
    
    request.session['pot_res'] = check_diceset(request.session['game_round'].refresh_state())
    
    return render_to_response("kniffel/kniffel.html",
                          {'playername': request.user,
                           'gamename': request.session['game'].name,
                           'diceset': request.session['diceset'],
                           'pot_res': request.session['pot_res'],
                           'sess': request,
                           'hold_w_id': hold_w_id,
                           'wurf': request.session['game_round'].wurf,
                           },
                            context_instance=RequestContext(request))  

    


@csrf_protect
def highscore(request):
    #highscore_list = game.objects.all().order_by('start')[3:]
    highscore_list = result.objects.all()[3:]
    
    latest_game_list = game.objects.all().order_by('start')[:3]
    latest_player_list = player.objects.all().order_by('id')[3:]
    t = loader.get_template('kniffel/highscore.html')
    c = Context({
        'highscore_list': highscore_list,
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
