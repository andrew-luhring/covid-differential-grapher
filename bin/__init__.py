#!/usr/bin/env python
import json
import jsonpickle
from helpers import Helpers
from fips import Fips
from statistics import Statistics
from master_obj import MasterObj
from populate import populate

populated = populate()
stats = Statistics(populated)
days_since_start = len(populated.listDates())

for item in stats.cases:
    print(item)
