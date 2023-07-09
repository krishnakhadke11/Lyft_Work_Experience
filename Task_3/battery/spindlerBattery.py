from battery.abcBattery import abcBattery
from battery.years import years

class spindlerBattery(abcBattery):
    def __init__(self, last_service_date,current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        
    def needs_service(self):
        yrObj = years()
        return yrObj.addYears(self.last_service_date,2)< self.current_date 