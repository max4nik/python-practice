from abc import ABC, abstractmethod
import time


class AbstractParent(ABC):

    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError

    @abstractmethod
    def cook(self, meal):
        raise NotImplementedError


class Mother(AbstractParent):

    def __init__(self, age):
        self.age = age
        print("mother constructor")

    def do_work(self):
        print("I`m working")

    def cook(self, meal):
        print("Cooking " + meal)
        time.sleep(1000)
        print("READY!")

    def do_house_work(self):
        print("listening to music")


class Father(AbstractParent):

    def __init__(self):
        print("father constructor")

    def play_guitar(self):
        print("play guitar")

    def do_house_work(self):
        print("sitting on the sofa and drinking beer")


class Friend:
    pass


class Daughter(Mother, Father):
    def __init__(self, age=0):
        Mother.__init__(self, age=age)
        Father.__init__(self)

    def hello_friend(self):
        pass

    def do_work(self):
        print("I`m working hard")

    def cook(self, meal):
        print("I can`t cook(((")


def greet_mother(mother: Mother):
    print("hello mother!")
    mother.do_work()


def greet_father(father: Father):
    print("time for beer!!!")
    father.play_guitar()


if __name__ == '__main__':
    daughter = Daughter()

    # changing parent here
    # daughter.__class__ = Friend

    greet_father(daughter)
    greet_mother(daughter)
    daughter.hello_friend()
    daughter.do_house_work()

    # list
    povtorka_list = ["phizra", "istoriya"]

    for x in [daughter]:
        x.do_house_work()

    # tuple
    vasian = ("11 years", 12, 13.4, daughter)

    # set
    my_set = {1, 4, 8, 8, "leet"}

    # frozen set
    not_my_set = frozenset(("di", "mi", "pi"))

    # dictionary
    my_dict = {1: "first", 2: "second", 3: "third?", (1, 2, 3): "tuple_as_key"}
