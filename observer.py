from abc import ABCMeta, abstractmethod
class Observer(metaclass=ABCMeta):
    # 观察者基类

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    # 被观察者基类

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    # 热水器
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print ("当前温度是: " + str(self.__temperature) + "℃")
        self.notifyObservers()


class washingMode(Observable):
    # 洗澡模式

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() < 70:
            print('水已经烧好，可洗澡.')

class DrinkingMode(Observer):
    # 饮水模式

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >=100:
            print('水烧开了, 可以饮用了.')




def testWaterHeater():
    heater = WaterHeater()
    washingObser = washingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)

testWaterHeater()