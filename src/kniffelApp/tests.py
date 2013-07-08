"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from kniffelApp.models import *  # @UnusedWildImport



class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class UnitTest(TestCase):
    def check_player_instance(self):
        """
        Test ob eine Instanz erstellt werden kann
        """
        newplayer = player()
        print newplayer.nick
        self.assertIsInstance(newplayer, player, "Player newplayer ist eine Instanz")

class test_complete(TestCase):
    def check_all(self):
        """
        Test ob eine Instanz erstellt werden kann
        """
        x = True
        self.assertTrue(x, "Test funktioniert") 

class test_instanz(TestCase):
    def test_instanz_create(self):
        """
        Test ob eine Instanz erstellt werden kann
        """
        ins = instanz()
        #x = ins.new_game()
        
        #self.assertIsInstance(x, instanz, "Ist eine Instanz")    
        self.assertIsInstance(ins, instanz, "Ist eine Instanz")    
    
    def test_instanz_new(self):
        ins = instanz()
        x = ins.new_game()
        self.assertIsInstance(x, instanz, "Ist eine Instanz")    
        
    
'''         
         
class testcase_createinstance(TestCase):
    def setUp(self):
        #instance.objects.create()
        #self.assertTrue(expr, msg)
        return True
        
'''