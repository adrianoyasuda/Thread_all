from multiprocessing.managers import BaseManager
import sys
import time

class QueueManager(BaseManager):
    pass

QueueManager.register('get_queue_numeros',callable=lambda:queue)
QueueManager.register('get_queue_respostas',callable=lambda:queue)

m = QueueManager(address=('localhost',50000),authkey=b'abc')
m.connect()
queueNumeros = m.get_queue_numeros()
queueRespostas = m.get_queue_respostas()
while True:
    msg=queueNumeros.get()
    print(msg)
    resp=msg-1
    queueRespostas.put((msg,resp))