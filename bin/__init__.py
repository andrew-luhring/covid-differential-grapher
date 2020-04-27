#!/usr/bin/env python
from statistics import Statistics
from populate import populate

populated = populate()
days_since_start = len(populated.listDates())
stats = Statistics(populated)


# result = {'data': stats.__dict__}
# for item in stats.cases:
    # print(item)

import jsons
converted = jsons.dump(stats)

import json
with open('data.json', 'w') as outfile:
    json.dump(converted, outfile)
