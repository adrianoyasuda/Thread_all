from threading import Thread
import random

NBITS=20

def verificaPrimo(n):
    count=0
    for i in range(n-1,1,-1):
        if i != None:
            if n%i == 0:
                count=1
                break

    if(count==0):
        print("{} é primo".format(n))
    else:
        print("{} não é primo".format(n))


if __name__ == "__main__":
    
    numeros=[]
    threads=[]
    for i in range(5):
        n = random.getrandbits(NBITS)
        print("Verificando {}".format(n))
        numeros.append(n)
        t = Thread(target=verificaPrimo,args=(n,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    print("Finalizado...")
        
    