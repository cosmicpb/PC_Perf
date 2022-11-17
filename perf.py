import time
import math

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
    if(prime==100000):
        break

tm2 = time.perf_counter()

print(primes[99999])
print(f'Tempo total: {tm2-tm1:0.2f} seconds')    

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
    if(prime==100000):
        break

tm2 = time.perf_counter()

print(primes[99999])
time1 = tm2-tm1
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
    if(prime==100000):
        break

tm2 = time.perf_counter()

print(primes[99999])
time2 = tm2-tm1
print(f'Tempo total: {tm2-tm1:0.2f} seconds') 
print('time1 (com print): ' + str(time1))
print('time2: (sem print) ' + str(time2))

