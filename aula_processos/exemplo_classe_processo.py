from multiprocessing import Process

#criando um classe que representa um processo
class MeuProcesso(Process):

    #inicilizacao do processo
    def __init__(self):
        Process.__init__(self)
    

    #tudo o que o processo irá executar deve
    #estar no método run. Enquanto o run estiver
    #rodando, o processo está em execução
    def run(self):
        print("Eu sou um processo!!! {} id={}".format(self.name,self.pid))

if __name__ == "__main__":
    
    processo = MeuProcesso()
    processo.start()
    processo.join()

    print("Pai finalizando...")
