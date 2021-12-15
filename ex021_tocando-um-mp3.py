from pygame import mixer
import formatos


formatos.entrada(21)

mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Digite a tecla que quiser para parar...')
mixer.music.stop()

formatos.saida(21)
