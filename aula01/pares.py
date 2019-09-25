

def ehPar(num):
    return (num % 2) == 0 


if __name__ == '__main__':
    for i in range(1,100):
        print("{} é par? {}".format(i,ehPar(i)))


