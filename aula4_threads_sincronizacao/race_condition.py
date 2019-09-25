from threading import Thread

acumulador=0
repeticoes=100000

def incrementa():
    global acumulador
    acumulador += 1

def decrementa():
    global acumulador
    acumulador -= 1
def incrementador():
    for i in range(repeticoes):
        incrementa()

def decrementador():
    for i in range(repeticoes):
        decrementa()

if __name__=="__main__":

    t1 = Thread(target=incrementador)
    t2 = Thread(target=decrementador)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Resultado final:{}".format(acumulador))