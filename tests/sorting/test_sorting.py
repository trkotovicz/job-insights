import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"min_salary": 1000, "max_salary": 5000, "date_posted": "2022-10-01"},
        {"min_salary": 5000, "max_salary": 10000, "date_posted": "2022-10-05"},
        {"min_salary": 3000, "max_salary": 6000, "date_posted": "2022-10-10"},
        {"min_salary": 10000, "max_salary": 50000, "date_posted": "2022-10-20"}
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == 1000
    assert jobs[3]["min_salary"] == 10000

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == 50000
    assert jobs[3]["max_salary"] == 5000

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2022-10-20"
    assert jobs[3]["date_posted"] == "2022-10-01"
