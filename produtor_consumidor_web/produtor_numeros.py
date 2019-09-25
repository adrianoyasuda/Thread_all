from multiprocessing import Process,Queue
from multiprocessing.managers import BaseManager
import time
import random


class Produtor(Process):

    def __init__(self, queue, *args, **kwargs):
        super(Process, self).__init__(*args, **kwargs)
        self.queue = queue

    def run(self):
        while(True):
            n = random.randint(1,400000)
            self.queue.put(n)
            time.sleep(1)