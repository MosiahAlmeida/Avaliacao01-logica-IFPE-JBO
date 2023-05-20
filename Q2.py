venceu = 0
perdeu = 0
for partidas in range (1,7):
    resultado =input().strip()
    if resultado == 'V':
        venceu += 1
    if resultado == 'P':
        perdeu += 1
if venceu == 5 or venceu == 6:
    print(1)
elif venceu == 3 or venceu == 4:
    print(2)
elif venceu == 1 or venceu == 2:
    print(3)
elif venceu ==0:
    print(-1)
    
