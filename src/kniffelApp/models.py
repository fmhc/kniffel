# -*- coding: latin-1 -*-
from django.db import models

import datetime
import random
from django.contrib.auth.models import User
from xmlrpclib import DateTime
from django.utils import timezone
from django.db.models.base import Model
from django.test import TestCase
   

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
 
    def startgame(self):
        
        for plyr in self.player.all():
            x = result()
            x.game = self.pk
            x.player.entry_set.add(plyr)
            x.save()
            
        self.runde = 1
        self.save()
        
        while self.runde < 14:
            for plyr in self.player.all():
                print "Runde " + self.runde
                act_res = result.objects.filter(player=plyr.pk,game=self.pk)
                print act_res.objects.all()
                inp = input("naechste Runde (y/n)")
                
                if inp == "y":
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
    player = models.ManyToManyField(player, related_name='p+')
    game = models.ForeignKey(game, related_name='g+')
    
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
    def checkbonus(self):
        rsum1 = self.r1er + self.r2er + self.r3er + self.r4er + self.r5er + self.r6er
        if (rsum1 >= 63):
            self.rbonus = 35
            self.save()
            return self.rbonus
        else:
            self.rbonus = 0
            return False

    
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
    
    def new(self):
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
        #newinstance = instance.objects.new()
        
        
        
'''

'''
class instanz(models.Model):
    activegame = models.ForeignKey(game, related_name='ga+', null=True)
    def new(self):
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
    def new(self, gamename=None, player1=None, player2=None, player3=None, player4=None):
        # neue Instanz erstellen
        
        self.activegame = game()
        self.activegame.name = raw_input("Spielname: ")
        self.activegame.save()    
        self.save()
   
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
            self.activegame.player.add(newplayer)
            
            i = i + 1
        return self
        