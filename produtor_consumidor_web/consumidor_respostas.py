from multiprocessing import Process,Queue
from multiprocessing.managers import BaseManager
import time
import random
import psycopg2

class Consumidor(Process):
    
    def __init__(self, queue, *args, **kwargs):
        super(Process, self).__init__(*args, **kwargs)
        self.queue = queue
    
    def run(self):
        conn = psycopg2.connect("dbname=ppd_aula6 host=localhost password=SenhaComplexa user=user")
        cur = conn.cursor()
        cont=0
        while(True):
            resp = self.queue.get()
            msg="Mensagem:{}->{}".format(resp[0],resp[1])
            cur.execute("INSERT INTO mensagens(msg) VALUES (%s) RETURNING id",(msg,))
            id_new = cur.fetchone()[0]
            conn.commit()
            cont+=1
            if(cont>=100):
                cur.execute("DELETE FROM mensagens where id<{}".format(id_new))
                conn.commit()  
                cont=0