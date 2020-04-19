import unittest
from populate import populate, count_lines, filestring


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


unittest.main(verbosity=2)
