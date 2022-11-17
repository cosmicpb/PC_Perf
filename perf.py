import time
import math

cpu = input('Digite seu Processador (i5, i7, Celeron, AMD): ')
gen = input('Digite a geração/outras configs do seu Processador: ')
ram = input('Digite a quantidade de RAM do seu PC (em GB): ')

max_value = 50000

cont = 0
prime = 0
i = 1
primes = []
tm1 = time.perf_counter()
while(True):
    iUp = i+1
    cont = 0
    for j in range(int(math.sqrt(i+1))):
        jUp = j+1
        if(iUp%jUp == 0):
            cont+=1
        if(cont>=2):
            break
    if(cont==1):
        print('PRIMO: ' + str(iUp) + '         NB:' + str(prime))
        primes.append(iUp)
        prime+=1
    i+=1
    if(prime==max_value):
        break

tm2 = time.perf_counter()
time1 = tm2-tm1
print(primes[max_value-1])
print(f'Tempo total: {tm2-tm1:0.2f} seconds')    

print('...')
print('Espere, rodando o mesmo algoritmo sem print')
print('...')

cont = 0
prime = 0
i = 1
primes = []
tm1 = time.perf_counter()
while(True):
    iUp = i+1
    cont = 0
    for j in range(int(math.sqrt(i+1))):
        jUp = j+1
        if(iUp%jUp == 0):
            cont+=1
        if(cont>=2):
            break
    if(cont==1):
        primes.append(iUp)
        prime+=1
    i+=1
    if(prime==max_value):
        break

tm2 = time.perf_counter()

print(primes[max_value-1])
time2 = tm2-tm1
print(f'Tempo total: {tm2-tm1:0.2f} seconds') 
print('------------------------------------------------------')
print(' ')
print('CPU: ' + cpu)
print('    ' + gen)
print('RAM: ' + ram + ' GB')
print(' ')
print('Tempo 1 (com print): ' + str(time1))
print('Tempo 2 (sem print): ' + str(time2))

