class ViewModel():
    def __init__(self):
        viewList = []

    def getState(self):
        pass
    def setState(self):
        pass
    
    def attach(self,view):
        self.viewList.append(view)
    def deatach(self,view):
        self.viewList.remove()
    def notify(self):
        for view in self.viewList :
            view.update()
    
