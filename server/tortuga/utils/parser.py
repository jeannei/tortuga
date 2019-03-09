"""
Parsing utilities
"""

import csv
from collections import defaultdict

SYMPTOMS_CSV = '../fixtures/symptoms.csv'


def parse_symptoms_csv(path=SYMPTOMS_CSV):
    """
    Parse symptoms csv of the form:
    symptom, diagnosis1, diagnosis2, diagnosis3… diagnosisN

    Parameters:
    arg1 (string): path to csv

    Returns:
    dictionary: dictionary with list as values
    """

    results = defaultdict(list)
    with open(path, mode='r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            key = ""
            for index, col in enumerate(row):
                if index == 0:
                    key = col
                else:
                    results[key].append(col.strip())
    return results
