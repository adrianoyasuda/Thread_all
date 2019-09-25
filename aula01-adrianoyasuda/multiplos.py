# coding=utf-8
ta = 0
tb = 0

for n in range(1, 1000):
    a = 3 * n
    ta = ta + a

    b = 5 * n
    tb = tb + b

print ("Soma dos Multiplos de 3: {}".format(ta))
print ("Soma dos Multiplos de 5: {}".format(tb))
