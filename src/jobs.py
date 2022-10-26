from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as file:
        jobs_data = csv.DictReader(file)
        return [*jobs_data]
