from abc import ABC,abstractmethod

class abcEngine(ABC):
    def __init__(self,last_service_date):
        self.last_service_date=last_service_date
    @abstractmethod    
    def engine_should_be_serviced(self):
        pass