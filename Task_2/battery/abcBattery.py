from abc import ABC,abstractmethod

class abcBattery(ABC):
    def __init__(self,last_service_date):
        self.last_service_date=last_service_date
        
    @abstractmethod
    def battery_needs_service(self):
        pass    
