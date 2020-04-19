
import unittest
from master_obj import MasterObj
from statistics import Statistics
from fips import Fips

class TestGetStatistics(unittest.TestCase):
    def test_diffs(self):
        stubmo = MasterObj()
        stubmo.addEntry('1234', '2020-01-21', Fips('ohio', 'seneca', 4, 1, '1234', '2020-01-21'))
        stubmo.addEntry('1234', '2020-01-22', Fips('ohio', 'seneca', 6, 1, '1234', '2020-01-22'))
        stubmo.addEntry('1234', '2020-01-23', Fips('ohio', 'seneca', 6, 2, '1234', '2020-01-23'))
        statistics = Statistics(stubmo).fipses
        self.assertEqual(statistics['1234'].case_differentials, [4, 2, 0])
        self.assertEqual(statistics['1234'].death_differentials, [1, 0, 1])

    def test_national_stats(self):
        stubmo = MasterObj()
        stubmo.addEntry('1234', '2020-01-21', Fips('ohio', 'seneca', 4, 1, '1234', '2020-01-21'))
        stubmo.addEntry('1234', '2020-01-22', Fips('ohio', 'seneca', 6, 1, '1234', '2020-01-22'))
        stubmo.addEntry('1234', '2020-01-23', Fips('ohio', 'seneca', 6, 2, '1234', '2020-01-23'))
        stubmo.addEntry('666', '2020-01-22', Fips('illinois', 'chicago', 6, 1, '666', '2020-01-22'))
        stubmo.addEntry('666', '2020-01-23', Fips('illinois', 'chicago', 6, 2, '666', '2020-01-23'))
        statistics = Statistics(stubmo)
        self.assertEqual(statistics.fipses['1234'].case_differentials, [4, 2, 0])
        self.assertEqual(statistics.fipses['666'].case_differentials, [6, 0])
        self.assertEqual(statistics.cases, [0, 4, 12, 12])
        self.assertEqual(statistics.case_differentials, [4, 8, 0])
        self.assertEqual(statistics.deaths, [0,1,2,4])
        self.assertEqual(statistics.death_differentials, [1,1,2])
        self.assertEqual(len(statistics.cases), 4)
        self.assertEqual(len(statistics.deaths), len(statistics.cases))
        self.assertEqual(len(statistics.case_differentials), 3)
        self.assertEqual(len(statistics.death_differentials), len(statistics.case_differentials))


unittest.main(verbosity=2)
