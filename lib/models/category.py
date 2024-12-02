class category:
    def __init__(self,name,id):
        self.name=name
        self.id = id 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value        
    @property
    def id(self):
        return self._id

    @name.setter
    def id(self, value):
        self._id = value        