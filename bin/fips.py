class Fips:
    def __init__(self, state, countyname, cases, deaths, fips, date):
        self.state = state
        self.county = countyname
        self.cases = int(cases)
        self.deaths = int(deaths)
        self.fips = fips
        self.date = date

    def toString(self):
        return f"On {self.date}, the county {self.county} in {self.state} had {self.cases} recorded cases and {self.deaths} people had died up until that point."
