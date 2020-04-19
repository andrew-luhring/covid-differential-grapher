import csv
from master_obj import MasterObj
from fips import Fips

filestring = "../covid-19-data/us-counties.csv"

exceptions = {
    'New York City' : 'nyc',
    'Kansas City': 'kcm'
}

def populate():
    mo = MasterObj()
    with open(filestring, newline='') as covid_csv:
        covid_data  = csv.DictReader(covid_csv)
        for row in covid_data:
            date = row['date'];
            fips = row['fips']
            state = row['state']
            county = row['county']
            cases = row['cases']
            deaths = row['deaths']
            if county in exceptions:
                fips = exceptions[county]

            if fips == '':
                fips = county + ' ' + state

            mo.addEntry(fips, date, Fips(state, county, cases, deaths, fips, date))

    return mo

def count_lines(filename):
    with open(filestring) as f:
        for i, l in enumerate(f):
            pass
        return i + 1
