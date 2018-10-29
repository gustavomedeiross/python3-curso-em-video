from pygame import mixer
mixer.init()
mixer.music.load('ex021song.mp3')
mixer.music.play()
input('Agora escuta?')