class Helpers:

    # given a master/tracking array, reverse the arrays and then sum their positions
    # This is used in Statistics to take all the counties where the death rates start on different days (so the array lengths all dont match)
    # and sum them into state level, county by county... so
    # Franklin County (started tracking earlier): [1,1,2,4], Seneca County [5,3,1] = [4+5, 3+2, 1+1, 1] = [9, 5, 2, 1]
    # this CHANGES THE VALUES OF THE MASTER ARRAY. Todo: make it not do that.
    @staticmethod
    def reverse_and_sum_elements_in_arrays(master, temp):
        for i, elem in enumerate(reversed(temp)):
            try:
                master[i] += elem
            except IndexError:
                master.append(elem)
        return master

    # given an array of numbers, return an array with the differences between them based on position
    # ex [1, 1, 2, 4, 8] returns [0,1,2,4]
    @staticmethod
    def getDiffs(array_of_numbers):
        diffs = []
        for pos, num in enumerate(array_of_numbers):
            if pos is 0:
                continue
            diffs.append(num - array_of_numbers[pos - 1])

        return diffs
