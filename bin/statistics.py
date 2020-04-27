from helpers import Helpers

class Statistic:
    def __init__(self, fips, cases, deaths, state):
        self.fips = fips
        self.cases = cases
        self.deaths = deaths
        self.case_differentials = Helpers.getDiffs(self.cases)
        self.death_differentials = Helpers.getDiffs(self.deaths)
        self.state = state

class Statistics:
    def __init__(self, mo):
        self.fipses = {}
        self.states = {}
        for fips in mo.fipses:
            if fips != 'null' and fips != '':
                cases_for_this_fips = [0]
                deaths_for_this_fips = [0]
                state = ''
                for date in mo.fipses[fips]:
                    cases_for_this_fips.append(date.cases)
                    deaths_for_this_fips.append(date.deaths)
                    state = date.state
            stat = Statistic(fips, cases_for_this_fips, deaths_for_this_fips, state)
            self.fipses[stat.fips] = stat

            if stat.state not in self.states:
                self.states[stat.state] = {'death_differentials': []}

            Helpers.reverse_and_sum_elements_in_arrays(self.states[stat.state]['death_differentials'], stat.death_differentials)


        for state in self.states:
            self.states[state]['death_differentials'] = self.states[state]['death_differentials'][::-1]

        self.cases = []
        self.case_differentials = []
        self.deaths = []
        self.death_differentials= []
        self.set_national(self.fipses)

    def get(self):
        return self.statistics

    @staticmethod
    def get_percentage_of_population(population, num):
        return round((num / population) * 100, 5)

    @staticmethod
    def get_percentage_of_population_in_array(population, arr):
        result = []
        for item in arr:
            result.append(Statistics.get_percentage_of_population(population, item))
        return result

    def set_national(self, populated_stats):
        for key in populated_stats:
            stat = populated_stats[key]
            # if len(stat.cases) <= 78:
            Helpers.reverse_and_sum_elements_in_arrays(self.cases, stat.cases)
            Helpers.reverse_and_sum_elements_in_arrays(self.case_differentials, stat.case_differentials)
            Helpers.reverse_and_sum_elements_in_arrays(self.deaths, stat.deaths)
            Helpers.reverse_and_sum_elements_in_arrays(self.death_differentials, stat.death_differentials)
        self.cases = self.cases[::-1]
        self.case_differentials = self.case_differentials[::-1]
        self.deaths = self.deaths[::-1]
        self.death_differentials = self.death_differentials[::-1]
