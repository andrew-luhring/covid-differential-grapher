import unittest
from helpers import Helpers
from statistics import Statistics
from populate import populate


class TestCheckDiffs(unittest.TestCase):
    def test_valid_diffs_positive(self):
        case = Helpers.getDiffs([1,2,5])
        expected = [1,3]
        self.assertEqual(case, expected)

    def test_negative_diffs(self):
        case = Helpers.getDiffs([1,0,5])
        expected = [-1, 5]
        self.assertEqual(case, expected);

    def test_empty(self):
        case = Helpers.getDiffs([])
        expected = []
        self.assertEqual(case, expected)

    def test_single(self):
        case = Helpers.getDiffs([1])
        expected = []
        self.assertEqual(case, expected)

class TestSumArrays(unittest.TestCase):
    def test_diffs(self):
        result = []
        obj = {'a': [1,1], 'b': [1,1,1], 'c': [1,1,1,1]}
        for key in obj:
            Helpers.reverse_and_sum_elements_in_arrays(result, obj[key])
        self.assertEqual([3,3,2,1], result)

    def test_stuff(self):
        _populated = populate()
        _stats = Statistics(_populated)
        _days_since_start = len(_populated.listDates())
        self.assertEqual(_days_since_start + 1, len(_stats.cases))


unittest.main(verbosity=2)
