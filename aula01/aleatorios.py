from random import randint

if __name__ == '__main__':

    #aleatorios = list()
    aleatorios = []
    #aleatorios = [1,2,3,4]

    for i in range(20):
        aleatorios.append(randint(1,10))
    
    print(aleatorios)
    print(aleatorios[0])
    print(len(aleatorios))
    print(aleatorios.index(1))
    print(aleatorios[2:6])
    print(aleatorios[-2])
    aleatorios.sort(reverse=True)
    print(aleatorios)

    for i,n in enumerate(aleatorios):
        print("{}-{}".format(i,n))


