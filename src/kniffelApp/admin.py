'''
Created on 03.07.2013

@author: fmh
'''

from django.contrib import admin
from kniffelApp.models import game, player, game_round, dice, result, instanz



admin.site.register(game)
admin.site.register(player)
admin.site.register(game_round)
admin.site.register(dice)
admin.site.register(result)
admin.site.register(instanz)