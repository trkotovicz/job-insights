from src.jobs import read


def get_unique_job_types(path):
    file = read(path)
    list = set()

    for job in file:
        list.add(job["job_type"])
    return list


def filter_by_job_type(jobs, job_type):
    list = []

    for job in jobs:
        if job["job_type"] == job_type:
            list.append(job)

    return list


def get_unique_industries(path):
    file = read(path)
    list = set()

    for industry in file:
        if industry["industry"] != "":
            list.add(industry["industry"])
    return list


def filter_by_industry(jobs, industry):
    list = []

    for job in jobs:
        if job["industry"] == industry:
            list.append(job)

    return list


def get_max_salary(path):
    file = read(path)
    jobs = []

    for job in file:
        if job["max_salary"].isnumeric():
            max_salary = int(job["max_salary"])
            jobs.append(max_salary)

    return max(jobs)


def get_min_salary(path):
    file = read(path)
    jobs = []

    for job in file:
        if job["min_salary"].isnumeric():
            min_salary = int(job["min_salary"])
            jobs.append(min_salary)

    return min(jobs)


def matches_salary_range(job, salary):
    min_salary = job.get("min_salary")
    max_salary = job.get("max_salary")

    if (
        "max_salary" not in job
        and "min_salary" not in job
        or type(min_salary) is not int
        or type(max_salary) is not int
        or type(salary) is not int
        or min_salary > max_salary
    ):
        raise ValueError

    return min_salary <= salary <= max_salary


def filter_by_salary_range(jobs, salary):
    list = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list.append(job)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    return list
