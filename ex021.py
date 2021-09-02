from pygame import mixer
print('{:=^100}'.format(' DESAFIO 21 '))
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Digite a tecla que quiser para parar...')
print('{:=^100}'.format(' FIM DESAFIO 21 '))