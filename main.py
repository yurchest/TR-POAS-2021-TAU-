import os
from SAU import *
import matplotlib.pylab as plt

os.chdir(os.path.dirname(os.path.realpath(__file__)))  # Задаем текущий каталог (откуда запускалась программа)

def write_in_file(x,y):
    fp = open('output.txt', 'w')
    for i in range(len(x)):
        stroka = str(i+1) + (len(str(len(x))) - len(str((i+1)))) * ' ' + 2*' ' + str(x[i]) + 3*' ' + str(y[i])
        fp.write(stroka + '\n')
    fp.close()

def show_graph(y):
    plt.xlabel('t')
    plt.ylabel('Выходной сигнал Y')
    plt.title('Переходной процесс САР')
    plt.plot(y)
    plt.show()

param = [3.0, -0.4, 0.2, 0.1, 0.05]
K1 = input('K1 = ')
K2 = input('K2 = ')

if K1: param[0] = float(K1)
if K2: param[1] = float(K2)


x = [0] * 5 + [1] * 1000   # Входной сигнал – «ступенька»
SAU = SAU(param)
y = []

for xt in x:
    SAU.zhach(xt)
    SAU.model()
    y.append(SAU.yhist[4])

write_in_file(x,y)

show_graph(y)





