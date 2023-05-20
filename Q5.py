numero = int(input())
divisores =0
for tentativa_d in range(1, numero+1):
    if  numero % tentativa_d ==0:
        divisores+=1
print(divisores)
