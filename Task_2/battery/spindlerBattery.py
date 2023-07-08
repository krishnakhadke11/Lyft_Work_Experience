from battery.abcBattery import abcBattery
import addYears

class spindlerBattery(abcBattery):
    def __init__(self, last_service_date,current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        
    def battery_needs_service(self):
        return addYears(self.last_service_date,2)< self.current_date 