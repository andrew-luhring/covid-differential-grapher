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
            self.fipses[fips] = []

        self.fipses[fips].append(self.dates[date][fips])

        self.entries+=1

    def listFips(self):
        return self.fipses.keys()

    def listDates(self):
        return self.dates.keys()

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


class Statistic:
    def __init__(self, fips, cases, deaths):
        self.fips = fips
        self.cases = cases
        self.deaths = deaths
        self.case_differentials = getDiffs(self.cases)
        self.death_differentials = getDiffs(self.deaths)

    # given a fips, go through each date and return an array of diffs for that place.
def getStatistics(mo):
    # gotta be a way to not do this n^2
    statistics = {}
    for fips in mo.fipses:
        if fips != 'null' and fips != '':
            cases_for_this_fips = [0]
            deaths_for_this_fips = [0]
            for date in mo.fipses[fips]:
                cases_for_this_fips.append(date.cases)
                deaths_for_this_fips.append(date.deaths)

        # this is also an n^2 operation
        stat = Statistic(fips, cases_for_this_fips, deaths_for_this_fips)
        statistics[stat.fips] = stat
    return statistics

populated = populate()
stats = getStatistics(populated)
days_since_start = len(populated.listDates())

def reverse_and_sum_elements_in_arrays(master, temp):
    for i, elem in enumerate(reversed(temp)):
        try:
            master[i] += elem
        except IndexError:
            master.append(elem)
    return master


def getNationalStatistics(populated_stats):
    master = {'cases': [], 'case_differentials': [], 'deaths': [], 'death_differentials':[]}
    # cant iterate forward because the data wont match up but if i iterate in reverse
    # it will, because if its in this db, it will
    # highest = 77
    for key in populated_stats:
        stat = populated_stats[key]
        # if len(stat.cases) <= 78:
        reverse_and_sum_elements_in_arrays(master['cases'], stat.cases)
        reverse_and_sum_elements_in_arrays(master['case_differentials'], stat.case_differentials)
        reverse_and_sum_elements_in_arrays(master['deaths'], stat.deaths)
        reverse_and_sum_elements_in_arrays(master['death_differentials'], stat.death_differentials)


    # print(highest)
    return {
        'cases': master['cases'][::-1],
        'case_differentials': master['case_differentials'][::-1],
        'deaths': master['deaths'][::-1],
        'death_differentials': master['death_differentials'][::-1]
    }

def percentage_of_population(arr):
    result = []
    for item in arr:
        result.append(round((item / 328200000) * 100, 5))

    return result


# print(len(stats))
national_statistics = getNationalStatistics(stats)
print('percentage of the US population who has died from covid 19:')
print(percentage_of_population(national_statistics['deaths'])[-1])
print('percentage of the US population who has gotten covid 19:')
print(national_statistics['cases'][-1], 'is', percentage_of_population(national_statistics['cases'])[-1])
# 328,200,000
# print(percentage_of_population([3282000]))
# print('death differentials')
# print(national_statistics['death_differentials'])

# 328.2m




percentage_of_population(national_statistics['deaths'])

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
        fip1 = Fips('ohio', 'seneca', 4, 1, fips, date)
        fip2 = Fips('ohio', 'seneca', 4, 1, fips, '2020-01-22')
        # 0 entries
        self.assertFalse(date in mo.dates)
        # 1 entry

        mo.addEntry(fips, date, fip1)
        self.assertTrue(date in mo.dates)
        # 1 fips
        self.assertTrue(fips in mo.fipses)
        # with 1 date
        self.assertTrue(fip1 in mo.fipses[fips])

        date2 = '2020-01-22'
        mo.addEntry(fips, date2, fip2)
        self.assertTrue(date in mo.dates)
        self.assertTrue(date2 in mo.dates)

        # still 1 fips
        # self.assertTrue(len(mo.fips.keys()) == 1)
        # but that fips now has 2 dates
        self.assertTrue(fip2 in mo.fipses[fips])
        self.assertTrue(fip1 in mo.fipses[fips])

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
        the_day_someone_i_maybe_know_fucking_died_of_coronavirus = 0
        populate_structure = populate()
        #{fips}
        self.assertTrue(hasattr(populate_structure, 'fipses'))
        #{fips: {[my hometown]}}]
        self.assertTrue(my_fucking_hometown in populate_structure.fipses)
        #{fips: {[my hometown]: [date someone died] : {} }}]
        seneca = populate_structure.fipses[my_fucking_hometown]
        self.assertTrue(populate_structure.fipses[my_fucking_hometown][the_day_someone_i_maybe_know_fucking_died_of_coronavirus])
        #{fips: { [my hometown] : { [date someone died]: {deaths, cases, state, etc} }}}]
        a_weird_fucking_day = seneca[the_day_someone_i_maybe_know_fucking_died_of_coronavirus]
        self.assertTrue(hasattr(a_weird_fucking_day, 'deaths'))

class TestGetStatistics(unittest.TestCase):
    def test_diffs(self):
        stubmo = MasterObj()
        stubmo.addEntry('1234', '2020-01-21', Fips('ohio', 'seneca', 4, 1, '1234', '2020-01-21'))
        stubmo.addEntry('1234', '2020-01-22', Fips('ohio', 'seneca', 6, 1, '1234', '2020-01-22'))
        stubmo.addEntry('1234', '2020-01-23', Fips('ohio', 'seneca', 6, 2, '1234', '2020-01-23'))
        statistics = getStatistics(stubmo)
        self.assertEqual(statistics['1234'].case_differentials, [4, 2, 0])
        self.assertEqual(statistics['1234'].death_differentials, [1, 0, 1])

    def test_national_stats(self):
        stubmo = MasterObj()
        stubmo.addEntry('1234', '2020-01-21', Fips('ohio', 'seneca', 4, 1, '1234', '2020-01-21'))
        stubmo.addEntry('1234', '2020-01-22', Fips('ohio', 'seneca', 6, 1, '1234', '2020-01-22'))
        stubmo.addEntry('1234', '2020-01-23', Fips('ohio', 'seneca', 6, 2, '1234', '2020-01-23'))
        stubmo.addEntry('666', '2020-01-22', Fips('illinois', 'chicago', 6, 1, '666', '2020-01-22'))
        stubmo.addEntry('666', '2020-01-23', Fips('illinois', 'chicago', 6, 2, '666', '2020-01-23'))
        statistics = getStatistics(stubmo)
        self.assertEqual(statistics['1234'].case_differentials, [4, 2, 0])
        self.assertEqual(statistics['666'].case_differentials, [6, 0])
        national_stats = getNationalStatistics(statistics)
        # self.assertEqual(national_stats.case_differentials, [4, 8, 0])
        self.assertEqual(national_stats['cases'], [0, 4, 12, 12])
        self.assertEqual(national_stats['case_differentials'], [4, 8, 0])
        self.assertEqual(national_stats['deaths'], [0,1,2,4])
        self.assertEqual(national_stats['death_differentials'], [1,1,2])
        self.assertEqual(len(national_stats['cases']), 4)
        self.assertEqual(len(national_stats['deaths']), len(national_stats['cases']))
        self.assertEqual(len(national_stats['case_differentials']), 3)
        self.assertEqual(len(national_stats['death_differentials']), len(national_stats['case_differentials']))

class TestSumArrays(unittest.TestCase):
    def test_diffs(self):
        result = []
        obj = {'a': [1,1], 'b': [1,1,1], 'c': [1,1,1,1]}
        for key in obj:
            reverse_and_sum_elements_in_arrays(result, obj[key])
        self.assertEqual([3,3,2,1], result)

    def test_stuff(self):
        self.assertEqual(days_since_start + 1, len(national_statistics['cases']))









unittest.main(verbosity=2)
