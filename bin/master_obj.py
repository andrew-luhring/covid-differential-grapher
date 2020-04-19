

"""
date,county,state,fips,cases,deaths
  dates: {
      [date]: {
          [fips]: {
              state, countyname, cases, deaths
          }
      }
  },
  fipses: {
      [fips]: [
          {state, countyname, cases, deaths},
          {state, countyname, cases, deaths}
      ]
  }
  """
class MasterObj:
    def __init__(self):
        self.dates = {}
        self.fipses = {}
        self.entries = 0

    def addEntry(self, fips, date, entry):
        if date not in self.dates:
            self.dates[date] = {}
        self.dates[date][fips] = entry

        if fips not in self.fipses:
            self.fipses[fips] = []

        self.fipses[fips].append(self.dates[date][fips])

        self.entries+=1

    def listFips(self):
        return self.fipses.keys()

    def listDates(self):
        return self.dates.keys()
