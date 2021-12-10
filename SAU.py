# Вариант 17
from elements import *

class SAU:
    def __init__(self, param):
        self.param = param
        # self.param[0] - K1
        # self.param[1] - K2
        # self.param[2] - T1
        # self.param[3] - T2
        # self.param[4] - T3

        self.yhist = [0] * 5
        # self.yhist[0] - состояние выхода на КЗ в момент времени - 1
        # self.yhist[1] - состояние выхода на КЗ в момент времени - 2
        # self.yhist[2] - состояние выхода на И в момент времени - 1
        # self.yhist[3] - состояние выхода на ИЗ в момент времени - 1
        # self.yhist[4] - состояние выхода У (К1) обратной свзязи в момент времени - 1

    def zhach(self, upr):
        self.x = upr

    def model(self):
        y1 = summator(usil(self.yhist[4], self.param[1]), self.x)
        y2 = koleb(y1, self.param[2], self.param[3], self.yhist[0], self.yhist[1])
        self.yhist[1] = self.yhist[0]
        self.yhist[0] = y2
        y3 = integr(y2, self.yhist[2])
        self.yhist[2] = y3
        y4 = inerz(y3, self.param[4], self.yhist[3])
        self.yhist[3] = y4
        y5 = usil(y4, self.param[0])
        self.yhist[4] = y5
