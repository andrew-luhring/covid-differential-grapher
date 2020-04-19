import unittest
from master_obj import MasterObj
from fips import Fips


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



unittest.main(verbosity=2)
