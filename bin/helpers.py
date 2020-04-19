class Helpers:

    @staticmethod
    def reverse_and_sum_elements_in_arrays(master, temp):
        for i, elem in enumerate(reversed(temp)):
            try:
                master[i] += elem
            except IndexError:
                master.append(elem)
        return master

    @staticmethod
    def getDiffs(array_of_numbers):
        diffs = []
        for pos, num in enumerate(array_of_numbers):
            if pos is 0:
                continue
            diffs.append(num - array_of_numbers[pos - 1])

        return diffs
