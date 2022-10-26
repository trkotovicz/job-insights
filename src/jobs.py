from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as file:
        file_reader = csv.DictReader(file)
        list = [row for row in file_reader]
    return list
