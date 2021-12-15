from pygame import mixer
from time import sleep
import formatos


formatos.entrada(41)

mixer.init()
mixer.music.load('ex041.mp3')
mixer.music.play()
sleep(1)
for i in range(10, -1, -1):
    print(i)
    sleep(2)
print('FELIZ ANO NOVO!!')
sleep(5)
formatos.saida(41)
