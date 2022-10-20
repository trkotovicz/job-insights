from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        file_reader = csv.DictReader(file)
        list = [row for row in file_reader]
    return list

    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
