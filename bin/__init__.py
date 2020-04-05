#!/usr/bin/env python
import csv
import json
import jsonpickle

filestring = "../covid-19-data/us-counties.csv"


def getDiffs(array_of_numbers):
    diffs = []
    for pos, num in enumerate(array_of_numbers):
        if pos is 0:
            continue
        diffs.append(num - array_of_numbers[pos - 1])

    return diffs


# date,county,state,fips,cases,deaths
#   dates: {
#       [date]: {
#           [fips]: {
#               state, countyname, cases, deaths
#           }
#       }
#   },
#   fipses: {
#       [fips]: [
#           {state, countyname, cases, deaths},
#           {state, countyname, cases, deaths}
#       ]
#   }
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
            self.fipses[fips] = {}

        if date not in self.fipses[fips]:
            # it should be pointing to the same instance. no reason to duplicate memory
            self.fipses[fips][date] = self.dates[date][fips]

        self.entries+=1

    def listFips(self):
        return self.fipses.keys()

    def listDates(self):
        return self.dates.keys()

class Fips:
    def __init__(self, state, countyname, cases, deaths, fips):
        self.state = state
        self.county = countyname
        self.cases = cases
        self.deaths = deaths
        self.fips = fips

    def toString(self):
        return f"The county {self.county} in {self.state} has {self.cases} recorded cases and {self.deaths} people have died."

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
            mo.addEntry(fips, date, Fips(state, county, cases, deaths, fips))

    return mo


class Statistics:
    def __init__(self, fips):
        self.fips = fips

    # given a fips, go through each date and return an array of diffs for that place.
def listIncreases():
    mo = MasterObj()

    for fips in mo.fipses:
        prevDate






listIncreases()



import unittest

def count_lines(filename):
    with open(filestring) as f:
        for i, l in enumerate(f):
            pass
        return i + 1



class TestCheckDiffs(unittest.TestCase):
    def test_valid_diffs_positive(self):
        case = getDiffs([1,2,5])
        expected = [1,3]
        self.assertEqual(case, expected)

    def test_negative_diffs(self):
        case = getDiffs([1,0,5])
        expected = [-1, 5]
        self.assertEqual(case, expected);

    def test_empty(self):
        case = getDiffs([])
        expected = []
        self.assertEqual(case, expected)

    def test_single(self):
        case = getDiffs([1])
        expected = []
        self.assertEqual(case, expected)

class TestAddEntry(unittest.TestCase):
    def test_add_multiple(self):
        mo = MasterObj()
        date = '2020-01-21'
        fips = '1234'
        # 0 entries
        self.assertFalse(date in mo.dates)
        # 1 entry

        mo.addEntry(fips, date, Fips('ohio', 'seneca', 4, 1, fips))
        self.assertTrue(date in mo.dates)
        # 1 fips
        self.assertTrue(fips in mo.fipses)
        # with 1 date
        self.assertTrue(date in mo.fipses[fips])

        date2 = '2020-01-22'
        mo.addEntry(fips, date2, Fips('ohio', 'seneca', 4, 1, fips))
        self.assertTrue(date in mo.dates)
        self.assertTrue(date2 in mo.dates)

        # still 1 fips
        # self.assertTrue(len(mo.fips.keys()) == 1)
        # but that fips now has 2 dates
        self.assertTrue(date2 in mo.fipses[fips])
        self.assertTrue(date in mo.fipses[fips])

class TestPopulate(unittest.TestCase):
    def test_same_length(self):
        populate_test = populate()
        self.assertEqual(populate_test.entries + 1, count_lines(filestring))

    def test_dates_structure(self):
        my_fucking_birthday_is_seriously_the_first_day_in_this_data = '2020-01-21'
        populate_structure = populate()
        #{dates}
        self.assertTrue(hasattr(populate_structure, 'dates'))
        #{dates:{[date]}}
        self.assertTrue(my_fucking_birthday_is_seriously_the_first_day_in_this_data in populate_structure.dates)
        #{dates:{ [date]: { [fips] }}}
        self.assertTrue('53061' in populate_structure.dates[my_fucking_birthday_is_seriously_the_first_day_in_this_data])
        #{dates:{ [date]: { [fips]: state, countyname, deaths, etc }}}
        snohomish = populate_structure.dates[my_fucking_birthday_is_seriously_the_first_day_in_this_data]['53061']
        self.assertTrue(hasattr(snohomish, 'state'))
        self.assertTrue(hasattr(snohomish, 'deaths'))
        self.assertTrue(hasattr(snohomish, 'cases'))

    def test_fips_structure(self):
        my_fucking_birthday_is_seriously_the_first_day_in_this_data = '2020-01-21'
        my_fucking_hometown = '39147'
        the_day_someone_i_maybe_know_fucking_died_of_coronavirus = '2020-03-31'
        populate_structure = populate()
        #{fips}
        self.assertTrue(hasattr(populate_structure, 'fipses'))
        #{fips: {[my hometown]}}]
        self.assertTrue(my_fucking_hometown in populate_structure.fipses)
        #{fips: {[my hometown]: [date someone died] : {} }}]
        seneca = populate_structure.fipses[my_fucking_hometown]
        self.assertTrue(the_day_someone_i_maybe_know_fucking_died_of_coronavirus in populate_structure.fipses[my_fucking_hometown])
        #{fips: { [my hometown] : { [date someone died]: {deaths, cases, state, etc} }}}]
        a_weird_fucking_day = seneca[the_day_someone_i_maybe_know_fucking_died_of_coronavirus]
        self.assertTrue(hasattr(a_weird_fucking_day, 'deaths'))

class TestListIncreases(unittest.TestCase):
    def test_same_length(self):
        increases = {
            'fipses': {
                '1234': {
                    '2020-01-21': Fips('ohio', 'seneca', 4, 1, '1234'),
                    '2020-01-22': Fips('ohio', 'seneca', 6, 1, '1234'),
                    '2020-01-23': Fips('ohio', 'seneca', 6, 2, '1234')
                }
            },
            'dates': {
                '2020-01-21': Fips('ohio', 'seneca', 4, 1, '1234'),
                '2020-01-22': Fips('ohio', 'seneca', 6, 1, '1234'),
                '2020-01-23': Fips('ohio', 'seneca', 6, 2, '1234'),
            }
        }

























unittest.main(verbosity=2)
