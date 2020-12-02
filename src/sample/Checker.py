from sample.Player import Player

class Checker:
    def __init__(self):
        self.player = Player()
    
    def remainder(self, file):
        time = self.player.getTime()

        if time > 17:
            self.player.playWavFile(file)