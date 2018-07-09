from view import ViewMain
from view import ViewPeriod

import datetime

class Controller:
    def __init__(self):

        pass
    def run(self):
        self.show(ViewPeriod.ViewPeriod(self,
                                        datetime.date.today().__str__(),
                                        datetime.date.today().__str__())
                             )
        self.show(ViewMain.ViewMain(self))
        pass
    def show (self, view):
            view.show()

if __name__ == "__main__":


    controller = Controller()
    controller.run()
