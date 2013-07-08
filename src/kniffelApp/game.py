'''
Created on 06.07.2013

@author: fmh
'''

from models import *
from django.core.context_processors import request
from django.contrib import sessions

def game_prep():
    session_instanz = instanz()
    #session_instanz.new_game(gamename, player1, player2, player3, player4)
    
    #newgame = session_instanz.new_game("Testspiel", "Player1")
    newgame = session_instanz.new_game()
    #newgame.startgame()
    
    for plyr in newgame.player.all():
        x = result()
        #x.save()
        x.game = newgame 
        x.player = plyr
        x.save()
            
    newgame.runde = 1
    newgame.save()
    
    newgame.play()
