import unittest 
from unittest.mock import *
from sample.Checker import Checker


class TestChecker(unittest.TestCase):

    def test_checker_before_17(self):
        checker = Checker()
        fileTest = "File.wav"
        checker.player.getTime = Mock(name = "getTime")
        checker.player.getTime.return_value = 12
        
        checker.player.wavWasPlayed = Mock(name = "wavWasPlayed")
        checker.player.wavWasPlayed.return_value = False

        result = checker.player.wavWasPlayed(fileTest)
        self.assertEqual(result, False)
    
    def test_checker_after_17(self):
        checker = Checker()
        fileTest = "File.wav"
        checker.player.getTime = Mock(name = "getTime")
        checker.player.getTime.return_value = 21
        
        checker.player.wavWasPlayed = Mock(name = "wavWasPlayed")
        checker.player.wavWasPlayed.return_value = True

        result = checker.player.wavWasPlayed(fileTest)
        self.assertEqual(result, True)

