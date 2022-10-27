from src.jobs import read


def get_unique_job_types(path):
    jobs_data = read(path)
    types_jobs_list = set()
    for job in jobs_data:
        job_type = job["job_type"]
        if job_type != "":
            types_jobs_list.add(job_type)
    return types_jobs_list


def filter_by_job_type(jobs, job_type):
    filter_job_type = [job for job in jobs if job["job_type"] == job_type]
    return filter_job_type


def get_unique_industries(path):
    jobs_data = read(path)
    industry_list = set()
    for job in jobs_data:
        industry = job["industry"]
        if industry != "":
            industry_list.add(industry)
    return industry_list


def filter_by_industry(jobs, industry):
    filter_industry = [job for job in jobs if job["industry"] == industry]
    return filter_industry


def get_max_salary(path):
    jobs_data = read(path)
    max_salary_list = list()
    for job in jobs_data:
        if job["max_salary"].isnumeric():
            max_salary = int(job["max_salary"])

            max_salary_list.append(max_salary)
    return max(max_salary_list)


def get_min_salary(path):
    jobs_data = read(path)
    min_salary_list = list()
    for job in jobs_data:
        if job["min_salary"].isnumeric():
            min_salary = int(job["min_salary"])

            min_salary_list.append(min_salary)
    return min(min_salary_list)


def matches_salary_range(job, salary):
    try:
        lower_salary = job.get("min_salary")
        higher_salary = job.get("max_salary")
    except KeyError:
        raise ValueError
    salary_data = set([type(lower_salary), type(higher_salary), type(salary)])
    if type(salary) != int or len(salary_data) != 1:
        raise ValueError
    elif lower_salary > higher_salary:
        raise ValueError
    else:
        return lower_salary <= salary <= higher_salary

    """Checks if a given salary is in the salary range of a given job
    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job
    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise
    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    salary_list = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_list.append(job)
        except ValueError:
            pass
    return salary_list
    """Filters a list of jobs by salary range
    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter
    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
