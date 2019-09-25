import threading
import time


def funcao(i, nome):

    time.sleep(2)
    print("{} - Imprimindo {}".format(threading.currentThread().getName(), i))

if __name__=="__main__":

    threads=[]
    for a in range(5):
        t=threading.Thread(target=funcao, args=(a, '5'))
        t.start()
        threads.append(t)
    
    print("Oiiii")
    print("Oiiii")

