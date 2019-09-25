from threading import Thread,Lock
import time
import random

acumulador=0
repeticoes=5
lock=Lock()

def incrementa():
    
    lock.acquire()
    global acumulador
    acumulador+=1
    lock.release()

    t = random.randint(1,20)
    print("INC - Dormindo por {}s".format(t))
    time.sleep(t)
    

def decrementa():

    lock.acquire()
    global acumulador
    acumulador-=1
    lock.release()

    t = random.randint(1,20)
    print("DEC - Dormindo por {}s".format(t))
    time.sleep(t)
    
def incrementador():
    #lock.acquire()
    for i in range(repeticoes):
        incrementa()
    #lock.release()

def decrementador():
    #lock.acquire()
    for i in range(repeticoes):
        decrementa()
    #lock.release()

if __name__=="__main__":

    t1 = Thread(target=incrementador)
    t2 = Thread(target=decrementador)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Resultado final:{}".format(acumulador))