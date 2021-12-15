import formatos


formatos.entrada(48)

s = 0
for i in range (1, 501, 2):
    if i % 3 == 0:
        s += i
print(s)

formatos.saida(48)
