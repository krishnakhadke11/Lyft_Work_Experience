from battery.abcBattery import abcBattery
import addYears

class nubbinBattery(abcBattery):
    def __init__(self, last_service_date,current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
    
    def needs_service(self):
        return addYears(self.last_service_date,4)< self.current_dlaate     