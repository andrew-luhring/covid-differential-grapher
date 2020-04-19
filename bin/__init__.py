#!/usr/bin/env python
from statistics import Statistics
from populate import populate

populated = populate()
days_since_start = len(populated.listDates())
stats = Statistics(populated)


for item in stats.cases:
    print(item)
