# -*- coding: latin-1 -*-
from django.db import models

import datetime
import random
from django.contrib.auth.models import User
from xmlrpclib import DateTime
from django.utils import timezone
from django.db.models.base import Model
from django.test import TestCase
from unittest import case
   

class playerManager(models.Manager):
    def create_player(self, nick):
        new_player = player.objects.create_player(nick=nick)
        return new_player
    
    
class player(models.Model):
    nick = models.CharField(max_length=200, null=True)
    user = models.ManyToManyField(User, related_name='u+', null=True, default=None)
    #objects = playerManager()
        
    def __unicode__(self):
        if (self.nick):
            return self.nick
        else:
            return "NoName"
    
    
class game(models.Model):
    
    start = models.DateTimeField(null=True, auto_now = True)
    end = models.DateTimeField(null=True, default=None)
    name = models.CharField(max_length=200, null=True, default='New Game')
    runde = models.IntegerField(default=0)
    player = models.ManyToManyField(player, related_name='pl+', null=True)
    #activeplayer = None
    
    #def __init__(self):
        #x = player()
        #x.nick = "New Player"
        #x.save()
        #self.player.entry_set.add(x)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('start',)
       
#    player = [(player()), player(), player(), player()]        
    #player = [(player()), player()]
 
    def play(self):
        
#        for plyr in self.player.all():
#            x = result()
#            x.game = self
#            x.player.entry_set.add(plyr)
#            x.save()
#        self.runde = 1
#        self.save()
       
        while self.runde < 14:
            for plyr in self.player.all():
                print "[Spieler " + str(plyr) + "]"
                print "[Runde " + str(self.runde) + "]"                
                #result.objects.get(player__id=1, game__id=1)
                act_res = result.objects.get(player__id=plyr.pk, game__id=self.pk)
                pot_res = result()
                ro = game_round()
                
                #wuerfeln
                diceset = ro.roll()
                print u"[1. Versuch] Würfelergebnis: " 
                print diceset
                           
                answer = raw_input("neuer Versuch")
                if str(answer).lower() in ['y', 'yes']:
                    
                    # noch mal rollen?
                    diceset = ro.roll()
                    print "[2. Versuch]"
                    print diceset
                    
                    answer = raw_input("neuer Versuch")
                    if str(answer).lower() in ['y', 'yes']:
                        
                        # noch ein drittes mal rollen?
                        diceset = ro.roll()
                        print "[3. Versuch]"
                        print diceset

                   
                pot_res.r1er = c1er(diceset) 
                pot_res.r2er = c2er(diceset) 
                pot_res.r3er = c3er(diceset) 
                pot_res.r4er = c4er(diceset) 
                pot_res.r5er = c5er(diceset) 
                pot_res.r6er = c6er(diceset) 
                pot_res.rbonus = cbonus(act_res)
                pot_res.r3p = c3p(diceset) 
                pot_res.r4p = c4p(diceset) 
                pot_res.rfullhouse = cfullhouse(diceset) 
                pot_res.rkleinestr = ckleinestr(diceset) 
                pot_res.rfgrossestr = cgrossestr(diceset)
                pot_res.rkniffel = ckniffel(diceset)
                pot_res.rchance = cchance(diceset)
                        
                print "potentielle ergebnisse"
                print "[1] - 1er"
                print act_res.r1er
                if act_res.r1er == None:
                    print pot_res.r1er 
                else:
                    print str(act_res.r1er) + " x"
                print "[2] - 2er"
                print act_res.r2er
                if act_res.r2er == None:
                    print pot_res.r2er 
                else:
                    print str(act_res.r2er) + " x"
                print "[3] - 3er"
                print act_res.r3er
                if act_res.r3er == None:
                    print pot_res.r3er 
                else:
                    print str(act_res.r3er) + " x"
                print "[4] - 4er"
                print act_res.r4er
                if act_res.r4er == None:
                    print pot_res.r4er 
                else:
                    print str(act_res.r4er) + " x"
                print "[5] - 5er"
                print act_res.r5er
                if act_res.r5er == None:
                    print pot_res.r5er 
                else:
                    print str(act_res.r5er) + " x"
                print "[6] - 6er"
                print act_res.r6er
                if act_res.r6er == None:
                    print pot_res.r6er 
                else:
                    print str(act_res.r6er) + " x"
                #print "x - Bonus"
                #print pot_res.rbonus 
                print pot_res.r3p 
                print pot_res.r4p 
                print pot_res.rfullhouse 
                print pot_res.rkleinestr 
                print pot_res.rfgrossestr
                print pot_res.rkniffel
                print pot_res.rchance 
                
                
                
                bla = 1
                
                
                def u1er():
                    if act_res.r1er == None:
                        act_res.r1er = pot_res.r1er
                        bla = 0
                    act_res.rbonus = cbonus(act_res)
                    print "1er gewaehlt"
                 
                def u2er():
                    if act_res.r2er == None:
                        act_res.r2er = pot_res.r2er
                        bla = 0
                    act_res.rbonus = cbonus(act_res)
                    print "2er gewaehlt"
                    
                def u3er():
                    if act_res.r3er == None:
                        act_res.r3er = pot_res.r3er
                        bla = 0
                    act_res.rbonus = cbonus(act_res)
                    print "3er gewaehlt"
                    
                def u4er():
                    if act_res.r4er == None:
                        act_res.r4er = pot_res.r4er
                        bla = 0
                    act_res.rbonus = cbonus(act_res)
                    print "4er gewaehlt"
                 
                def u5er():
                    if act_res.r5er == None:
                        act_res.r5er = pot_res.r5er
                        bla = 0
                    act_res.rbonus = cbonus(act_res)
                    print "5er gewaehlt"
                    
                def u6er():
                    if act_res.r6er == None:
                        act_res.r6er = pot_res.r6er
                        bla = 0
                    act_res.rbonus = cbonus(act_res)
                    print "1er gewaehlt"        
                                               
                options = { 1 : u1er,
                            2 : u2er,
                            3 : u3er,
                            4 : u4er,
                            5 : u5er,
                            6 : u6er,
                            }
                
                while bla == 1:
                    huhu = input("Wo setzen?")
                    options[huhu]()
                    
                print "ergebnisse"
                print act_res.r1er 
                print act_res.r2er 
                print act_res.r3er 
                print act_res.r4er 
                print act_res.r5er 
                print act_res.r6er 
                print act_res.rbonus 
                print act_res.r3p 
                print act_res.r4p 
                print act_res.rfullhouse 
                print act_res.rkleinestr 
                print act_res.rfgrossestr
                print act_res.rkniffel
                print act_res.rchance 
                
                act_res.save()
                inp = raw_input("naechste Runde (y/n)")
                
                if (inp == str('y')):
                    print "naechster spieler..."
                else:
                    print "dann nicht..."
                    
            self.nextround()
        return True
        
    
    def player_list(self):
        return self.player.all()
        #return True
    
    def nextround(self):   
        self.runde = self.runde + 1
        return True #runden
    
    def laufzeit(self):
        if (self.end):
            return self.end - self.start
        else:
            return datetime.datetime.now() - self.start
    
    def ende(self):
        self.end = datetime.datetime.now()
        self.save()





class result(models.Model):
    game = models.ForeignKey(game, related_name='g+')
    player = models.ForeignKey(player, related_name='p+')
    
    r1er = models.IntegerField(null=True) # 1er: es werden nur 1er gezaehlt
    r2er = models.IntegerField(null=True) # 2er: es werden nur 2er gezaehlt
    r3er = models.IntegerField(null=True) # 3er: es werden nur 3er gezaehlt
    r4er = models.IntegerField(null=True) # 4er: es werden nur 4er gezaehlt
    r5er = models.IntegerField(null=True) # 5er: es werden nur 5er gezaehlt
    r6er = models.IntegerField(null=True) # 6er: es werden nur 6er gezaehlt
    rbonus = models.IntegerField(null=True) # 35 Punkte Bonus, wenn die oberen Punkte >= 63 sind
    r3p = models.IntegerField(null=True) # Dreierpasch
    r4p = models.IntegerField(null=True) # Viererpasch
    rfullhouse = models.IntegerField(null=True) # full house
    rkleinestr = models.IntegerField(null=True) # 1-2-3-4, 2-3-4-5, oder 3-4-5-6 30 Punkte
    rfgrossestr = models.IntegerField(null=True) # 1-2-3-4-5 oder 2-3-4-5-6 40 Punkte
    rkniffel = models.IntegerField(null=True) # Fuenf gleiche Wuerfel 50 Punkte
    rchance = models.IntegerField(null=True) # Alle Augen zaehlen
    
    def sum_oben(self):
        return 0
    
    def sum_unten(self):
        return 0

    
def OfAKind(dice, n):
    return HighestRepeated(dice,n) * n

def HighestRepeated(dice, minRepeats):
    unique = set(dice)
    repeats = [x for x in unique if dice.count(x) >= minRepeats]
    return max(repeats) if repeats else 0

def SumOfSingle(dice, selected):
    return dice.count(selected) * selected

def cchance(dice):
    return sum(dice)
 
def cfullhouse(dice):
    return OfAKind(dice, 2)
 
def c3p(dice):
    return OfAKind(dice, 3)
 
def c4p(dice):
    return OfAKind(dice, 4)
 
def ckleinestr(dice):
    return 15 if tuple(sorted(dice)) == (1,2,3,4,5) else 0
 
def cgrossestr(dice):
    return 20 if tuple(sorted(dice)) == (2,3,4,5,6) else 0
 
def c1er(dice):
    return SumOfSingle(dice,1)
 
def c2er(dice):
    return SumOfSingle(dice,2)
 
def c3er(dice):
    return SumOfSingle(dice,3)
 
def c4er(dice):
    return SumOfSingle(dice,4)
 
def c5er(dice):
    return SumOfSingle(dice,5)
 
def c6er(dice):
    return SumOfSingle(dice,6)
 
def ckniffel(dice):
    return 50 if len(dice) == 5 and len(set(dice)) == 1 else 0

def cbonus(res):
        rsumme = 0
        if (res.r1er != None):
            rsumme = rsumme + res.r1er
        if (res.r2er != None):
            rsumme = rsumme + res.r2er
        if (res.r3er != None):
            rsumme = rsumme + res.r3er
        if (res.r4er != None):
            rsumme = rsumme + res.r4er
        if (res.r5er != None):
            rsumme = rsumme + res.r5er
        if (res.r6er != None):
            rsumme = rsumme + res.r6er
        
        #rsum1 = res.r1er + res.r2er + res.r3er + res.r4er + res.r5er + res.r6er
        if (rsumme >= 63):
            res.rbonus = 35
            #self.save()
            return res.rbonus
        else:
            res.rbonus = 0
            return 0
            
def checkall(dice):
    
    return False



class dice(models.Model):
    hold = models.BooleanField(default=False)
    value = models.IntegerField(default=0)
    
    def hold(self):
        self.hold = 1
        return self.hold
    def roll(self):
        self.value = random.randint(1,6)
        return self.value
    def __init__(self):
        self.hold = False
        self.value = 0
        return None
    def __unicode__(self):
#        return models.Model.__str__(self):
        return self.value

        
class game_round(models.Model):
    game = models.ForeignKey(game, related_name='g+')
    w1 = models.ForeignKey(dice, related_name='w1+')
    w2 = models.ForeignKey(dice, related_name='w2+')
    w3 = models.ForeignKey(dice, related_name='w3+')
    w4 = models.ForeignKey(dice, related_name='w4+')
    w5 = models.ForeignKey(dice, related_name='w5+')
    w1 = dice()
    w2 = dice()
    w3 = dice()
    w4 = dice()
    w5 = dice()
    wurf = models.IntegerField(default=1)
    state = [0, 0, 0, 0, 0]
    
    def refresh_state(self):
        statea = [self.w1.value,
                  self.w2.value,
                  self.w3.value,
                  self.w4.value,
                  self.w5.value]
        self.state = statea
        return statea
    
    def check(self):
        # self.state
        ergebnis = [0, 0, 0, 0, 0]
        return ergebnis
    
    
    
    def roll(self):
        if ( self.wurf <= 3 ):
            self.wurf = self.wurf + 1
            if not ((self.w1.hold)): self.w1.roll()
            if not ((self.w2.hold)): self.w2.roll()
            if not ((self.w3.hold)): self.w3.roll()
            if not ((self.w4.hold)): self.w4.roll()
            if not ((self.w5.hold)): self.w5.roll()
            
            return self.refresh_state()
        else:
            return "Es wurde schon drei mal gewuerfelt"

'''        
class instance(models.Model):
    #activegame = models.ForeignKey(game, related_name='ga+', null=True)
    activegame = game()
    #objects = instanceManager()
    
    def new_game(self):
        # neue Instanz erstellen
        myinstance = instance()
        myinstance.activegame = game()
        myinstance.activegame.name = raw_input("Spielname: ")
        myinstance.activegame.save()    
        myinstance.save()
   
        # Anzahl Spieler festlegen
        i = 0
        anzahl = int(raw_input(u"Spieleranzahl: "))
        while i < anzahl:
#            newplayer.nick = str(raw_input(u"Name fuer Spieler" + str(i) + ": "))        
            #nickname = "New Player"
            #dynamicplayertext = "Name für Spieler "+str(i)
            #nick = input(dynamicplayertext)      
            #str(nickname)  
            nickname = str(raw_input("Spielername: "))
            
            print u"%s hinzugefügt", nickname
            #newplayer = player.objects.create_player("'"+str(nick)+"'")
            #newplayer.save()
            #self.mygame.player.entry_set.add(newplayer)
            newplayer = player(nick=nickname)
            newplayer.save()
            myinstance.activegame.player.add(newplayer)
            
            i = i + 1
        return myinstance
        

    
class processchecker(models.Model):
    if not (instance.objects.all()):    
        print "es rennt keine instanz"
        #newinstance = instance.objects.new_game()
        
        
        
'''

'''
class instanz(models.Model):
    activegame = models.ForeignKey(game, related_name='ga+', null=True)
    def new_game(self):
        # neue Instanz erstellen
        myinstance = instanz()
        myinstance.activegame = game()
        myinstance.activegame.name = raw_input("Spielname: ")
        myinstance.activegame.save()    
        myinstance.save()
   
        # Anzahl Spieler festlegen
        i = 0
        anzahl = int(raw_input(u"Spieleranzahl: "))
        while i < anzahl:
#            newplayer.nick = str(raw_input(u"Name fuer Spieler" + str(i) + ": "))        
            #nickname = "New Player"
            #dynamicplayertext = "Name für Spieler "+str(i)
            #nick = input(dynamicplayertext)      
            #str(nickname)  
            nickname = str(raw_input("Spielername: "))
            
            print u"%s hinzugefügt", nickname
            #newplayer = player.objects.create_player("'"+str(nick)+"'")
            #newplayer.save()
            #self.mygame.player.entry_set.add(newplayer)
            newplayer = player(nick=nickname)
            newplayer.save()
            myinstance.activegame.player.add(newplayer)
            
            i = i + 1
        return myinstance
'''

        
        
              
class instanz(models.Model):
    activegame = models.ForeignKey(game, related_name='ga+', null=True)
    def new_game(self, gamename=None, player1=None, player2=None, player3=None, player4=None):
        # neue Instanz erstellen
        self.activegame = game()
        if ( gamename != None ):
            self.activegame.name = gamename
        else:
            self.activegame.name = raw_input("Spielname: ")
        
        self.activegame.save()    
        
        # Anzahl Spieler festlegen
        if ( player1 != None ):
                nickname = str(player1)
                newplayer = player(nick=nickname)
                newplayer.save()
                self.activegame.player.add(newplayer)
                if ( player2 != None ):
                    nickname = str(player2)
                    newplayer = player(nick=nickname)
                    newplayer.save()
                    self.activegame.player.add(newplayer)
                if ( player3 != None ):
                    nickname = str(player3)
                    newplayer = player(nick=nickname)
                    newplayer.save()
                    self.activegame.player.add(newplayer)
                if ( player4 != None ):
                    nickname = str(player4)
                    newplayer = player(nick=nickname)
                    newplayer.save()
                    self.activegame.player.add(newplayer)
                
        else:
            i = 0
            anzahl = int(raw_input(u"Spieleranzahl: "))
            while i < anzahl:
    #            newplayer.nick = str(raw_input(u"Name fuer Spieler" + str(i) + ": "))        
                #nickname = "New Player"
                #dynamicplayertext = "Name für Spieler "+str(i)
                #nick = input(dynamicplayertext)      
                #str(nickname)  
                nickname = str(raw_input("Spielername: "))
                
                print u"%s hinzugefügt", nickname
                #newplayer = player.objects.create_player("'"+str(nick)+"'")
                #newplayer.save()
                #self.mygame.player.entry_set.add(newplayer)
                newplayer = player(nick=nickname)
                newplayer.save()
                self.activegame.player.add(newplayer)
                
                i = i + 1
                
                
        self.activegame.save()    
        self.save()
        return self.activegame
        