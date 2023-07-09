class years:
    def addYears(self,date,addYears):
        self.addedYears = date.replace(year=date.year + addYears)
        return self.addedYears