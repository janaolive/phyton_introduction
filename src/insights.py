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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    jobs_data = read(path)
    industry_list = set()
    for job in jobs_data:
        industry = job["industry"]
        if industry != "":
            industry_list.add(industry)
    return industry_list


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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
    return []
